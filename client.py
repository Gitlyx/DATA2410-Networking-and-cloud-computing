import socket


def client(IP, PORT, BOT):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, int(PORT)))
    print(
        f"Connected to port {PORT} with IP {IP} running bot name {BOT} ")

    # Communication receiver.
    print(client_socket.recv(1024).decode())

    # Communication sender.
    while True:
        message = f'{socket.gethostname()}: '
        message += input(message)
        client_socket.send(message.encode())
