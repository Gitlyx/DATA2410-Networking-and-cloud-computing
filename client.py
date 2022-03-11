import socket
import sys
import threading
from time import sleep

# IP = sys.argv[1]
# PORT = int(sys.argv[2])
# BOT = sys.argv[3]


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

print(IP)
print(PORT)
print(BOT)

def activate_bot():
    botlogic = ''


def activate_user():
    while True:
        sleep(1)
        message = input("You: ")
        client_socket.send(("You: " + message).encode())


if BOT:
    threading.Thread(target=activate_bot).start()
else:
    threading.Thread(target=activate_user).start()

def recieve():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)


threading.Thread(target=recieve).start()