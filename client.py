import re
import socket
import sys
import threading
import response


HOST = socket.gethostname()
PORT = 2345
USER = sys.argv[1]


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def bot_response(message):
    word_list = re.split(r'\s+|[,;?!.]\s*', message.lower())
    word_found = False
    verb = ''

    for action in response.action_list:
        for word in word_list:
            if word == action:
                word_found = True
                verb = word

    if word_found:
        bot_response = f'🟩 {response.positive(verb)}'
    else:
        bot_response = f'🟥 {response.negative()}'

    return bot_response


def bot_mode():
    print(f'Chat bot has been launched with name {USER}')

    while True:
        message = client_socket.recv(1024).decode()
        user_reply = message.split()

        if user_reply[0].lower() == 'user:':
            response = bot_response(message)
            client_socket.send(f'{USER}: \t{response}'.encode())


def user_mode():
    print(f'USER detected, launching entering chatroom as: {USER}')

    while True:
        response = input(f"\n{USER}: ")
        client_socket.send(f'{USER}: \t{response}'.encode())


if USER.lower() == 'user':
    threading.Thread(target=user_mode).start()
else:
    threading.Thread(target=bot_mode).start()
