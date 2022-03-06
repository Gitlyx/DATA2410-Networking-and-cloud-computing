import socket

# ----------------------------------------------------------------
# Client variabels, functions
client_list = []


def connect_client(client_socket, client_address):
    try:
        client_list.append(client_socket)
        client_socket.send('Connection successful.'.encode('utf8'))
        server_broadcast(
            f'IP: {client_address} has conncted to the server.')
    except:
        print('ERROR: Connection could not be established.')


def server_listener(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        server_broadcast(client_socket, message)


def server_broadcast(client_socket, message):

    for client in client_list:
        message = f'{client_socket}: {message}'
        client.send(message.encode('utf8'))

    server_commands(client_socket, message)


def server_commands(client_socket, message):
    if message == 'exit':
        server_broadcast(f'{client_socket} has left.')
        client_socket.send("Closing the server ...".encode('utf8'))
        client_socket.close()


# ----------------------------------------------------------------
# Connection variables
IP = '192.168.56.1'
PORT = 2345

# Socket implementation
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()

while True:
    print("Listening to connections ...")
    client_socket, client_address = server_socket.accept()
    connect_client(client_socket, client_address)
    server_listener(client_socket, client_address)
