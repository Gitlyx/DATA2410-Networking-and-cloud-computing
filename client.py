
import re
import socket
import sys
import threading
from time import sleep
import event

# All these variables can be replaced with sys.arg[int] to add input parameters.
USER_NAME = sys.argv[1] if len(sys.argv) >= 2 else event.random_botname()
HOST = socket.gethostname()
PORT = 2345

client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_connection.connect((HOST, PORT))

################################################################
# This code block handles the connection logic in the client.
# Whenever a name is given a role is specified based on the name given.
################################################################


def connect_client(USER_NAME):
    # Registers the clients username on the server.
    username = USER_NAME.capitalize()
    client_connection.sendall(username.encode())

    if username.lower() == 'lord':
        threading.Thread(target=admin_recv).start()
        print(f'Connecting as Lord of the realm')
    else:
        threading.Thread(target=bot_recv).start()
        print(f'Connecting as {username}.')


################################################################
# This code block is assigned to the admin if named "Lord"
# This client profile has extended functionality and can write and post messages.
################################################################
def admin_recv():
    while True:
        try:
            # Listens to messages sent from the server.
            message = client_connection.recv(1024).decode()
            if message == 'request_input':
                threading.Thread(target=admin_send).start()
            else:
                print(f'{message}')
        except:
            print('Connection has been closed.')
            client_connection.close()
            break



def admin_send():
    while True:
        sleep(2)
        event.get_event()
        try:
            response = input('\nYou: ')
            client_connection.sendall(response.encode())
        except:
            client_connection.close()
            break


################################################################
# This code block is assigned to bots if not named "Lord"
# This client profile has automatic responses from listed in event.py.
################################################################
def bot_recv():
    while True:
        try:
            # Handles only mssages sent from the "Lord" and ignores the rest.
            message = client_connection.recv(1024).decode()
            user_reply = message.split()
            if user_reply[0].lower() == 'lord:':
                response = bot_send(message)
                client_connection.send(f'{response}'.encode())
        except:
            print('Connection has been closed.')
            client_connection.close()
            break


def bot_send(message):
    # Splits the message and stores it in an array while filtering away symbols using regex.
    word_list = re.split(r'\s+|[,;?!.]\s*', message.lower())

    # Loops through the array and compares with a list of actions imported from event.py
    for action in event.action_list:
        for word in word_list:
            if word == action or word == f'{action}ing':

                bot_response = f'🟩 {event.positive_response(word)}'
                return bot_response

    # If word is not found, return generic message.
    bot_response = f'🟥 {event.negative_response()}'
    return bot_response


connect_client(USER_NAME)
