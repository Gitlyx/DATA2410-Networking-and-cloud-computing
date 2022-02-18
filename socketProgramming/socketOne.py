from socket import (
    socket,
    AF_INET,
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

HOST, PORT = "127.0.0.1", 8080
response = b"HTTP/1.1 200 OK\r\nHello World"

with socket.socket(socket.AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        try:
            conn, addr = sock.accept()
            req = conn.recv(1024).decode()
            print(req)
            conn.sendall(response)
            conn.close()
        except Exception as E:
            print(E)
