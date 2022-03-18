
import re
import socket
import sys
import threading
from time import sleep
from tkinter import E
import response




HOST = socket.gethostname()
PORT = 2345
USER = sys.argv[1]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def start_client():
    set_username = f'{USER}'
    client_socket.sendall(set_username.encode())

    if USER.lower() == 'user':
        threading.Thread(target=client_recv).start()
        threading.Thread(target=client_send).start()
        print(f'\n{USER} has connected to the server. Listening to inputs ...')

    else:
        threading.Thread(target=bot_recv).start()
        print(f'\nBot with name {USER} has connected and now listening to responses ...'
    )

# This code block is active if the client is named "user". It recognizes that the user needs input options.
# User also has permission to execute commands.
def client_recv():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if len(message) > 0 :
                print(f'{message}', end='\n')
        except:
            print('Connection has been terminated.')
            client_socket.close()
            break
 

def client_send():
    while True :
        response = input()
        client_socket.sendall(response.encode())
        

# This code block is for bots. It detects if the variable USER is not initially set to user but anything else.
# BOT has the ability to respond to any command that the "user" has replied with.
def bot_recv():
    print('bot_recv() active.')

    while True:
        try:
            message = client_socket.recv(1024).decode()
            user_reply = message.split()
            if user_reply[0].lower() == 'user:' and user_reply[1].lower().find('-') != 0:
                response = bot_send(message)
                client_socket.send(response.encode())
        except:
            print('Connection has been terminated.')
            client_socket.close()
            break

def bot_send(message):
    word_list = re.split(r'\s+|[,;?!.]\s*', message.lower())
    word_found = False

    for action in response.action_list:
        for word in word_list:
            if word == action or word == f'{action}ing':
                word_found = True
                verb = word

    if word_found:
        bot_response = f'🟩 {response.positive(verb)}'
    else:
        bot_response = f'🟥 {response.negative()}'

    return bot_response
    

start_client()
