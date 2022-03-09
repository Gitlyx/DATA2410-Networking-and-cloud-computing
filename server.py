import socket
from _thread import *

# ----------------------------------------------------------------
# Client variabels, functions
client_list = []


def connect_client(client_socket, client_address):
    client_list.append(client_socket)
    client_socket.send('Connection successful.'.encode())
    broadcast(f'IP: {client_address} has conncted to the server.')


def broadcast(message):

    for client in client_list:
        message = f'{client_socket}: {message}'
        client.send(message.encode())


# ----------------------------------------------------------------
# Server socket implementation
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 2345))
server_socket.listen(4)
print("Listening to connections ...")

while True:
    client_socket, client_address = server_socket.accept()
    connect_client(client_socket, client_address)
    print(f'{client_address} has connected ')



