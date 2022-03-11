import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 2345))
server_socket.listen(4)
print("Server is listening ...")

client_list = []

    

def broadcast(message):
    print(message)
    for client in client_list:
        client.send(message.encode())


def listener(client):
    while True:
        try:
            response = client.recv(1024).decode()
            broadcast(response)
        except:
            client_list.remove(client)
            client.close()
            break


def server():
    while True:
        client_socket, client_address = server_socket.accept()
        client_list.append(client_socket)
        broadcast(f'Update: {client_address} has connected to the server.')

        thread = threading.Thread(target=listener, args=(client_socket,))
        thread.start()


server()
