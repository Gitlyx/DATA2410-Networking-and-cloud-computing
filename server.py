import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 2345))
server_socket.listen(4)
print("Server is listening ...")
client_list=[]

def broadcast(message):
    for client in client_list:
        client.send(message.encode())


def handle(client):
    while True:
        response = client.recv(1024).decode()
        broadcast(response)

def server():
    while True:
        client_socket, client_address = server_socket.accept()
        client_list.append(client_socket)
        print(f'Server: {client_address} has connected to the server.')
        broadcast(f'Server: {client_address} has connected to the server.')

        thread = threading.Thread(target=handle, args=(client_socket,))
        thread.start()

server()