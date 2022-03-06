import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 2345))

message = client_socket.recv(1024)
print(message.decode('utf8'))

while True:
    print('You: ', end='')
    command = input()
    client_socket.send(command.encode())
