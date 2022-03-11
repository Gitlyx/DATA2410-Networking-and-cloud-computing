import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 2345))
server_socket.listen(4)
print(
    '################################\n'
    'WELCOME TO THE COOLEST ROOM EVER!\n'
    '################################\n'
)

client_list = []


# Broadcasts messages to all clients allowing bots to respond.
def broadcast(message):
    print(message)
    for client in client_list:
        client.send(message.encode())


# Listener twith an exception handler that closes sockets in case the responses are fired off too fast.
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

        thread = threading.Thread(target=listener, args=(client_socket,))
        thread.start()


server()
