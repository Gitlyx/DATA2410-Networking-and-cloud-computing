#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "time.nist.gov"
    port = 13

    s.connect((host, port))
    s.sendall(b'')
    print("-------------------------------------------------------------------------")
    print(str(s.recv(4096), 'utf8'))
        print(str(s.recv(4096), 'utf8'))

