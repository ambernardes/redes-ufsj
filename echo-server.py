#!/usr/bin/env python3

import socket
import selectors

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Como solicitado, os registros vão ser armazenados em uma estrutura de lista, dicionário, etc
# Os dados são perdidos quando o servidor é fechado
local_people_database = []
# Variavel de controle que mantém o servidor de pé
shutdown_server = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    # Mantém o servidor aberto.
    while True:
        # A cada iteração do lopp
        conn, addr = s.accept()
        response = ""
        with conn:    
            print('Query recieved by ', addr)
            data = conn.recv(1024)
            
            # Caso o servidor receba uma solicitação vazia, o derruba
            if not data:
                break
            else:
                query = data.decode()
                print('Query recieved - ', query)

                # Processa as queries enviadas pelo cliente
                if query == "SELECT*" or query == "select*":
                    if len(local_people_database) == 0:
                        response = 'Database is empty. Please insert some data.'
                    else: 
                        for people in local_people_database:
                            response += "\t\t".join(people)+"\n"
                            
                elif "INSERT" in query or "insert" in query:
                    people_data = query.split(";")[1:]
                    
                    # Assumindo que todos os campos sejam obrigatórios
                    if len(people_data) == 3:
                        local_people_database.append(people_data)
                        response = 'Data Saved Successfully!\n'
                    else:
                        response = """Query is in the wrong format.\n
                                      The correct one is: 'INSERT;NAME;GENDER;AGE'\n"""
                elif query == ":q" or query == ":Q":
                    conn.sendall(b'Shutting down the server\n')
                    break
                else:
                    response = 'Try another query!\n'
                
                # Envia uma resposta ao cliente
                conn.sendall(response.encode())
