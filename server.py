import socket

# ----------------------------------------------------------------
# Client variabels, functions
client_list = []


def connect_client(client_socket, client_address):

    client_list.append(client_socket)
    client_socket.send('Connection successful.'.encode('utf8'))
    server_broadcast(f'IP: {client_address} has conncted to the server.')


def server_listener():
    while True:
        message = client_socket.recv(1024).decode('utf8')
        server_broadcast(message)


def server_broadcast(message):

    for client in client_list:
        message = f'{client_socket}: {message}'
        client.send(message.encode('utf8'))

    server_commands(client_socket, message)


def server_commands(client_socket, message):
    if message == 'exit':
        server_broadcast(f'{client_socket} has left.')
        client_socket.send("Closing the server ...".encode())
        client_socket.close()


# ----------------------------------------------------------------
# Socket implementation
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 2345))
server_socket.listen(5)
print("Listening to connections ...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f'{client_address} has connected ')
    connect_client(client_socket, client_address)
    server_listener()
