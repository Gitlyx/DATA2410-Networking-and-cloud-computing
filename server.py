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


# Listener with an exception handler that closes the socket and ends the thread upon error detection.
# This prevents the server from idling due to BrokenPipeErrors that occurs upon read/write error on sockets.
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

        threading.Thread(target=listener, args=(client_socket,)).start()


server()
