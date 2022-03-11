import socket
import threading
from time import sleep

IP = socket.gethostname()
PORT = 2345
BOT = None

print(IP)
print(PORT)
print(BOT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))


def initiate_bot():
    print('Bot ')


if BOT:
    initiate_bot()


def send():
    while True:
        sleep(1)
        message = input("You: ")
        client_socket.send(("You: " + message).encode())


def recieve():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)


threading.Thread(target=recieve).start()
threading.Thread(target=send).start()
