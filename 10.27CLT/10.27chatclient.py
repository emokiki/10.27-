import socket
import sys

import time

HOST = '127.0.0.1'
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    message = input('client : ')
    clientSocket.send(message.encode('utf-8'))
    response = clientSocket.recv(1024)
    print ('server : ', response.decode('utf-8'))
    message = "/0"

clientSocket.close()