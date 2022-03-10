import socket


client_list = []


def broadcast(message):
    for client in client_list:
        client.send(message.encode())


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.56.1', 2345))
server_socket.listen(4)
print("Listening to connections ...")

while True:
    client_socket, client_address = server_socket.accept()
    client_socket.send(
        'You have successfully connected to the server.'.encode())
    client_list.append(client_socket)
    broadcast(
        f'IP: {client_address} has conncted to the server.')
