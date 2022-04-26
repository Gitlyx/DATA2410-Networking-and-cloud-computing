import socket
import threading
from time import sleep

# Can be replaced with sys.arg[int] to accept CLI input parameter.
HOST = socket.gethostname()
PORT = 2345

server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.bind((HOST, PORT))
server_connection.listen(5)

connection_list = []
username_list = []


################################################################
# This code block is used to handle connections and threads that is applied to clients.
# Some of the cose that is nested within this block will be explained further down.
################################################################
def server_accept():
    print('\nChat server is online! \nNow listening to connections (0/5).\n')

    while len(username_list) < 5:
        try:
            # Accepts any new socket connections.
            client_connection, client_address = server_connection.accept()
            connection_list.append(client_connection)

            # Accepts first message "username" sent by the client and registers to array.
            client_username = client_connection.recv(1024).decode()
            username_list.append(client_username)

            # Each connection has its own thread listening to responses.
            threading.Thread(target=server_recv, args=(
                client_connection, client_username)).start()

            # Prints status on server and notifies the Lord of the realm
            server_broadcast(f"{client_username} has entered the realm.")
            print(f"{client_username} has connected ({len(username_list)}/5).")

        except:
            print('Server error, closing down.')
            server_connection.close()
            break

    print("\nThe server now has 5 active connections.")
    start_game()


def server_recv(client_connection, client_username):
    # Every message will pass a is_command check before being forwarded.
    while True:
        try:
            message = client_connection.recv(1024).decode()
            if len(message) > 0:
                if is_command(message):
                    find_command(client_connection, message)
                else:
                    message = f'{client_username}:\t {message}'
                    client_broadcast(client_connection, message)

        except:
            print(f'{client_username} has left the chat.')
            client_connection.close()
            break


def start_game():
    # Stops incoming connections and activates input on the admin client.
    server_connection.close()
    server_broadcast('request_input')

    # A Pleasant announcement to the admin client that the game has begun.
    server_broadcast(
        f'\n ---------- Welcome to the Game of Thrones ----------')
    server_broadcast(
        "You now have 5/5 individuals present in your domain to heeding your every command.")
    server_broadcast(
        "If you need assistance, --help will provide you with the information you need.")


################################################################
# This code block is to check and parse the commands to see which one will be invoked.
# In case there is errors during exection of the command, the user will get a feedback sent directly.
################################################################
def is_command(message):
    # If the message has three or less substring and includes symbols: '--'.
    if len(message.split()) < 3 and message.find('--') == 0:
        return True


def find_command(client_connection, message):
    if '--help' in message:
        response = '''
        This is the Game of Thrones, you are presented with a variety of actions can choose from. 
        If you dislike anyone from your team you can always ask them to leave them with --dismiss <name> 
        or even --leave, to terminate the session. With that said lets try again ..
        '''
        client_connection.sendall(response.encode())

    elif '--dismiss' in message and len(message.split()) == 2:
        target_username = message.split()[1]
        dismiss_username(client_connection, target_username)

    elif '--leave' in message:
        print("Server close down has been requested, shutting down the server.")
        response = '\nThe Lord has left the realm, everyone is allowed to leave.'
        server_broadcast(response)
        close_connections(client_connection)

    else:
        message = 'Unknown command. Try [--help/--leave/--dismiss <name>].'
        client_connection.sendall(message.encode())


def dismiss_username(client_connection, target_username):
    # Looks up if the requested username is in the list of active clients.
    if target_username in username_list:
        target_connection = get_connection(target_username)
        target_connection.close()

        connection_list.remove(target_connection)
        username_list.remove(target_username)

        server_response = f'You have dismissed {target_username}, {len(username_list)}/5 left on your team.'
        client_connection.sendall(server_response.encode())

    # If not the client is notified that the user does not exist.
    else:
        error_response = (
            f'There is no one on the realm named \'{target_username}\'.')
        client_connection.sendall(error_response.encode())
        print(
            f'ERROR: Could not find {target_username} in list of connections.')


def close_connections(client_connection):
    # This function terminates all the other clients first.
    for connection in connection_list:

        if connection != client_connection:
            username = get_username(connection)
            connection.close()
    # Then terminates the requesters connection.
    response = 'You have left the realm.'
    client_connection.sendall(response.encode())
    client_connection.close()


################################################################
# The remainder of this code block will consists of action that is called upon by the server.
# I chose to  separate these into smaller individual functions for better reusability and readability.
################################################################
def client_broadcast(client_connection, message):
    # Used by the server to distribute a message from the admin client.
    for connection in connection_list:
        if connection != client_connection:
            connection.sendall(message.encode())
            sleep(0.1)


def server_broadcast(message):
    # Used by the server to broadcast message to all clients.
    for connection in connection_list:
        connection.sendall(message.encode())
        sleep(0.1)


def get_username(client_connection):
    index = connection_list.index(client_connection)
    username = username_list[index]
    return username



def get_connection(username):
    index = username_list.index(username)
    client_connection = connection_list[index]
    return client_connection


server_accept()
