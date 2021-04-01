#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Recebe a query solicitado pelo usuário via terminal
print("-------------------------- Insert a query --------------------------")
print("-- SELECT* - To see the list of people on the sever ----------------")
print("-- INSERT;NAME;GENDER;AGE - To insert a new person on database -----")
print("-- :q - To quit ----------------------------------------------------")

query = input()
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(query.encode())
        data = s.recv(1024)
        print(data.decode())
        
        if query == ":q" or query == ":Q":
            print("Shutting down the client.")
            break
        
        query = input()
