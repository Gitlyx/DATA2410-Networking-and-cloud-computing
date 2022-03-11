import random
import socket
import sys
import threading
from time import sleep

HOST = 'localhost'
PORT = int(sys.argv[1])
USER = sys.argv[2]


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def bot_response(message):
    word_list = message.split()
    action_list = [
        'cook', 'eat', 'sleep', 'play', 'game', 'work', 'study',
        'fight', 'run', 'swim', 'drive', 'walk', 'exercize',
    ]

    verb = ''
    detected = False

    for action in action_list:
        for word in word_list:
            if word == action:
                detected = True
                verb = f'{word}ing'

    positive_response_list = [
        f'Wow, {verb}? My palms are sweaty ..',
        f'I can\'t handle {verb}, my knees are weak and arms are heavy.',
        f'Finally someone who likes {verb}, just let me grab my moms spaghetti.',
        f'I haven\'t tried {verb} before, but I promise I\'ll remain calm and ready. '
    ]

    negative_response_list = [
        f'I dont know what that is, can we do something else?',
        f'Haha, what planet are you from? We don\'t do that here 😂😂'
        f'What a strange request, I hope I never have to do that!',
        f'Not even my granny would do that!',
    ]

    if detected == True:
        response = f'🟩{random.choice(positive_response_list)}'
    else:
        response = f'🟥 {random.choice(negative_response_list)}'

    return response


def bot_mode():
    print('Initiating bot mode ...')

    while True:
        message = client_socket.recv(1024).decode()
        user_reply = message.split()

        if user_reply[0] == 'user:':
            response = bot_response(message)
            client_socket.send(f'{USER}:{response}'.encode())


def user_mode():
    print('Initiating user mode ...')

    while True:
        print('Taking responses')
        response = input(f"\n{USER}: ")
        print('Reponse taken')
        client_socket.send(f'{USER}: {response}'.encode())
        print('Reponse delivered')


if USER == 'user':
    threading.Thread(target=user_mode).start()
else:
    threading.Thread(target=bot_mode).start()
