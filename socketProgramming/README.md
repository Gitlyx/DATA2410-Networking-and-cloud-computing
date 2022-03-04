# DATA2410-Networking-and-cloud-computing
## Introduction
This is a library containing notes and files from the course DATA2410: Networking and cloud computing from OsloMet. Files and folders are subjected to change based on work and uploads across the duration of course this spring.

#### HTTP server
This creates a TCP Socket with default port of 8080 for running test 1.

``` python
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM,
    SO_REUSEADDR,
    SOL_SOCKET
)

HOST, PORT = "127.0.0.1", 8080
response = b"HTTP/1.1 200 OK\r\nHello World"

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
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
```


#### IP address
This fetches the local IP addres on the current host
``` python
#!/usr/bin/env python

import socket

ip = socket.gethostbyname('example.com')
print(ip)

```

#### UDP quote on client
This fetches a random quote generated on a server though User Datagram Protocol.
```python
#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "time.nist.gov"
    port = 13

    s.connect((host, port))
    s.sendall(b'')
    print(str(s.recv(4096), 'utf8'))

```

#### TCP Time and date
This fetches the time and date on a server through Transmission Control Protocol and displays it in the terminal.
```python
#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "time.nist.gov"
    port = 13

    s.connect((host, port))
    s.sendall(b'')
    print(str(s.recv(4096), 'utf8'))

```