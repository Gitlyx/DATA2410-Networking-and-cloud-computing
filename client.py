import socket
import threading

IP = socket.gethostname()
PORT = 2345
BOT = 'Charlie'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

def recieve():    
    while True:
        message = client_socket.recv(1024).decode()
        print(message);

def send():
    while True:
        message = (input('You: '))
        client_socket.send(message.encode())

threading.Thread(target=recieve).start()
threading.Thread(target=send).start()