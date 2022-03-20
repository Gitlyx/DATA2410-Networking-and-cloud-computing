
import re
import socket
import sys
import threading
from time import sleep
import response

HOST = socket.gethostname()
PORT = 2345
USER = sys.argv[1]

client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_connection.connect((HOST, PORT))


def connect_client():
    set_username = f'{USER}'
    client_connection.sendall(set_username.encode())

    if USER.lower() == 'user':
        threading.Thread(target=client_recv).start()
        threading.Thread(target=client_send).start()
        print(f'{USER} has connected to the server.')

    else:
        threading.Thread(target=bot_recv).start()
        print(f'Bot with name {USER} has connected to the server'
              )


def client_recv():
    while True:
        try:
            message = client_connection.recv(1024).decode()
            if len(message) > 0:
                print(f'{message}')
        except:
            print('Connection has been closed.')
            client_connection.close()
            break


def client_send():
    while True:

        response = input()
        client_connection.sendall(response.encode())


def bot_recv():
    print('bot_recv() active.')

    while True:
        try:
            message = client_connection.recv(1024).decode()
            user_reply = message.split()
            if user_reply[0].lower() == 'user:' and user_reply[1].lower().find('-') != 0:
                response = bot_send(message)
                client_connection.send(f'{response}'.encode())
        except:
            print('Connection has been closed.')
            client_connection.close()
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


connect_client()
