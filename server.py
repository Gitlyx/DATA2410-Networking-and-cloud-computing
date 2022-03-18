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

        #client.py automatically sends its username upon connection.
        username = client_socket.recv(1024).decode()
        username_list.append(username)

        broadcast_message(f"{username} has entered the chat.")
        print(f"{username} has entered the chat.")

        #Server will now have its own thead listening to the connected client.
        threading.Thread(target=server_recv, args=(client_socket,)).start()
    


# Listener with an exception handler that closes the socket and ends the thread upon error detection.
# This prevents the server from idling due to BrokenPipeErrors that occurs upon read/write error on sockets.
def server_recv(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if len(message) > 0 :
                if not command(client_socket,message): send_message(client_socket, message)
        except:
            client_socket.close()
            break


# This code block is functions that lets the server handle singular tasks.
# Functions are made to simplify the code and to easier understand what actinos the server is doing.
def broadcast_message(message):
    for client in client_list:
        client.sendall(message.encode())

def send_message(client_socket, message):
    # Find the username of the sending client.
    username = get_username(client_socket)
    message = f'{username}: {message}'
    for client in client_list:
        if client != client_socket and client_socket != "":
            client.sendall(message.encode())
    
    print(f'{message}', end='\n')


def get_username(client_socket):
    index = client_list.index(client_socket)
    username = username_list[index]
    return username

def get_client_socket(username):
    index = username_list.index(username)
    client_socket = client_list[index]
    return client_socket

def close_connection(client_socket, username):
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



# This code block handles the commands sent from the user if command criterias are met.
# The message is then parsed and checks if the server can handle any of the requests.
def command(client_socket,message):
    if len(message.split()) <= 2 and message.find('-') == 0:
        execute_commands(client_socket, message)


def execute_commands(client_socket, message):
    
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
        message = 'Unknown command. Try [--help/--exit].'
        client_socket.sendall(message.encode())

start_server()
