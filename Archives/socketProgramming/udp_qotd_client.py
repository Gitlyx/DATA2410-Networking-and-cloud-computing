#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    message = b''
    addr = ("djxmmx.net", 17)

    s.sendto(message, addr)

    data, address = s.recvfrom(1024)
    print(data.decode())
