import socket

IP = socket.gethostname()
PORT = 2345
BOT = 'Charlie'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
print(
    f"Connected to port {PORT} with IP {IP} running bot name {BOT} ")

# Communication receiver.
print(client_socket.recv(1024).decode())

# Communication sender.
while True:
    message = f'{socket.gethostname()}: '
    message += input(message)
    client_socket.send(message.encode())
