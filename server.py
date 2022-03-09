import socket


client_list = []


def broadcast(message):
    for client in client_list:
        client.send(message.encode())


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), 2345))
    server_socket.listen(4)
    print("Listening to connections ...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_socket.send('Connection successful.'.encode())
        client_list.append(client_socket)
        broadcast(
            f'IP: {client_address} has conncted to the server.')
