import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 2345))

# Communication receiver.
print(client_socket.recv(1024).decode())


while True:
    message = f'{socket.gethostname()}: '
    message += input(message)
    client_socket.send(message.encode())
