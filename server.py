import socket

# ----------------------------------------------------------------
# Client variabels, functions
client_list = []


def connect_client(client_socket, client_address):
    client_list.append(client_socket)
    client_socket.send('Connection successful.'.encode('utf8'))
    server_broadcast(f'IP: {client_address} has conncted to the server.')


def server_broadcast(message):

    for client in client_list:
        message = f'{client_socket}: {message}'
        client.send(message.encode())

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
server_socket.listen(4)
print("Listening to connections ...")

while True:
    client_socket, client_address = server_socket.accept()
    connect_client(client_socket, client_address)

    message = client_socket.recv(1024).decode()
    print(f'{client_address} has connected ')

    server_broadcast(message)
    print(f'{message}')
