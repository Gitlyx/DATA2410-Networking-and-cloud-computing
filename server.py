from pydoc import cli
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 2345))
server_socket.listen(4)
client_list = []
username_list = []

def start_server():
    print('Server has been started up.')
    print(f'Server now has 0/4 connections.\n')

    while True:
        count = len(client_list)
        client_socket, client_address = server_socket.accept()
        client_list.append(client_socket)

        # client.py automatically sends its username upon connection.
        username = client_socket.recv(1024).decode()
        username_list.append(username)

        broadcast_message(f"{username} has entered the chat.")
        print(f"{username} has entered the chat.")

        # Each connection has its own thread listening to responses.
        threading.Thread(target=server_recv, args=(client_socket,)).start()

# The server_recv is listening to any responses the client is sending. 
# The try/catch- block is implemented to close the connection upon errors such as infinite loops and BrokenPipe errors.
def server_recv(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if len(message) > 0 :
                if not command(client_socket,message): send_message(client_socket, message)
        except:
            client_socket.close()
            break


# I have broken down all frequently used tasks into functions for easier readability.
# These functions are made to more easily understand which tasks the server has to handle.
def broadcast_message(message):
    # Breoadcasts all the messages accross all connections.
    for client in client_list:
        client.sendall(message.encode())

def send_message(client_socket, message):
    # Sends our messages to other clients using "{username}: {message}" formatting.
    username = get_username(client_socket)
    message = f'{username}: {message}'
    for client in client_list:
        if client != client_socket and client_socket != "":
            client.sendall(message.encode())
    print(f'{message}', end='\n')

def get_username(client_socket):
    # Looks up which username each client has based on the matching connection data.
    index = client_list.index(client_socket)
    username = username_list[index]
    return username

def get_client_socket(username):
    # Looks up what connection data each user has based on their username.
    index = username_list.index(username)
    client_socket = client_list[index]
    return client_socket

def close_connection(client_socket, username):
    # Closes a single connection based on parameter: username. 
    if username in username_list:
        client_connection = get_client_socket(username)
        client_connection.sendall(f'{username} has been disconnected.'.encode())
        client_connection.close()        

        client_list.remove(client_connection)
        username_list.remove(username)
    else:
        response = (f'Could not find {username} in list of connections.')
        client_socket.sendall(response.encode())
        
def close_all_connections(client_socket):
    # Closes up all connections, allowing the user to be the last connection closed.
    for client in client_list:
        try:
            if client != client_socket:
                username = get_username(client)
                client.close()
                print(f'{username} has been terminated.')
        except:
            print(f'Error disconnecting {username}.')

    client_socket.sendall('Your connection has been temrinated.'.encode())
    client_socket.close()



# This code block is for handling commands sent from the user with "--" prefix.
# All the commands are made server side so that the server is able to handle all the clients indevidually.
def command(client_socket,message):
    # Checks if the message is a command by confirming that it is limited to max 2 substring AND as well as including the prefix "--".
    if len(message.split()) <= 2 and message.find('--') == 0:
        execute_commands(client_socket, message)


def execute_commands(client_socket, message):
    # Each command has to be an exact match, otherwise the user is promted to use one of the existing commands available.    
    if '--help' in message:
        response = 'Try communicating with the connected clients by suggesting an action such as "Anyone want to play a game?"'
        print(response)
        client_socket.sendall(response.encode())

    elif '--exit' in message:
        response = 'Exit command has been requested, closing down the server.'
        client_socket.sendall(response.encode())
        close_all_connections(client_socket)

    elif '--kick' in message and len(message.split()) == 2:
        username = message.split()[1]
        close_connection(client_socket, username)

    else:
        message = 'Unknown command. Try [--help/--exit/--kick \{username\}].'
        client_socket.sendall(message.encode())

start_server()
