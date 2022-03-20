from pydoc import cli
import socket
import threading
from time import sleep
from xmlrpc import client
import response

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 2345))
server_socket.listen()
connection_list = []
username_list = []

print('''
-------------------------------------------------------------
██     ██ ███████ ██       ██████  ██████  ███    ███ ███████ 
██     ██ ██      ██      ██      ██    ██ ████  ████ ██      
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████   
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██      
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████
--------------------------------------------------------------                                                                                                           
''')


def server_accept():
    while True:
        client_connection, client_address = server_socket.accept()
        connection_list.append(client_connection)

        # connection.py automatically sends its username upon connection.
        client_username = client_connection.recv(1024).decode()
        username_list.append(client_username)

        server_broadcast(f"{client_username} has entered the chat.")
        print(f"{client_username} has entered the chat.")

        # Each connection has its own thread listening to responses.
        threading.Thread(target=server_recv, args=(
            client_connection, client_username)).start()
        if len(connection_list) == 4:
            print('There are now 4 connections, you can start chatting with eachother, here is some actions you can use: ')
            print(response.action_list)


def server_recv(client_connection, client_username):
    while True:
        try:
            message = client_connection.recv(1024).decode()
            if len(message) > 0:
                if is_command(message):
                    translate_commands(client_connection, message)
                else:
                    message = f'{client_username}: {message}'
                    client_broadcast(client_connection, message)
                    print(f'{message}\r')
        except:
            print(f'{client_username} has left the chat.')
            client_connection.close()
            break

        return client_username


# I have broken down all frequently used tasks into functions for easier readability.
# These functions are made to more easily understand which tasks the server has to handle.
def server_broadcast(message):
    if not connection_list:
        for connection in connection_list:
            connection.sendall(message.encode())


def client_broadcast(client_connection, message):
    for connection in connection_list:
        if connection != client_connection and client_connection != "":
            connection.sendall(message.encode())


def get_username(client_connection):
    index = connection_list.index(client_connection)
    username = username_list[index]
    return username


def get_connection(username):
    index = username_list.index(username)
    client_connection = connection_list[index]
    return client_connection


def kick_username(client_connection, target_username):
    if target_username in username_list:
        target_connection = get_connection(target_username)
        target_connection.close()

        connection_list.remove(target_connection)
        username_list.remove(target_username)

        response = f'You have kicked {target_username}.'
        client_connection.sendall(response.encode())
    else:
        response = (
            f'Could not find {target_username} in list of connections.')
        client_connection.sendall(response.encode())


def close_connections(client_connection):
    for connection in connection_list:
        try:
            if connection != client_connection:
                username = get_username(connection)
                connection.close()
        except:
            print(f'Error disconnecting {username}.')

    response = 'Your connection has been terminated.'
    client_connection.sendall(response.encode())
    client_connection.close()


def is_command(message):
    if len(message.split()) <= 2 and message.find('--') == 0:
        return True


def translate_commands(client_connection, message):
    if '--help' in message:
        response = 'Try communicating with the connected clients by suggesting an action such as "Anyone want to play a game?"'
        client_connection.sendall(response.encode())

    elif '--kick' in message and len(message.split()) == 2:
        username = message.split()[1]
        kick_username(client_connection, username)

    elif '--exit' in message:
        print('\nExit command has been requested, closing down the server.')
        close_connections(client_connection)

    else:
        message = 'Unknown command. Try [--help/--exit/--kick \{username\}].'
        client_connection.sendall(message.encode())


server_accept()
