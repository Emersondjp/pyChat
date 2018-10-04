#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################################
## Description :
##
## Usage :
##
## Mentioin :
##
## Author : DingJianPing
## Date :
## Version :
########################################################

################### Begin Argument Parser #########################
import argparse
parser = argparse.ArgumentParser(description="your script description")
parser.add_argument('-s', '--server',  dest='serv', action='store', default='localhost', help='Server host name/ip address.')
parser.add_argument('-p', '--port', dest='port', action='store', default='21567', help='Server port.')

args = parser.parse_args()

#print(args)
##################### End Argument Parser ##########################

from socket import *
import os
from time import ctime
import threading

HOST = args.serv
PORT = eval(args.port)
BUFSIZ = 1024
SOCKQUEUEMAXSIZE = 5
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(SOCKQUEUEMAXSIZE)

clients = []
data = ''

def spread_data():
    global clients
    global data
    for client in clients:
        client.send(data)

def handle_request():
    global clients
    global data
    client_sock = clients[-1]
    while True:
        data = client_sock.recv(BUFSIZ)
        if not data:
            client_sock.close()
            data = 'One client closed.'.encode()
            t = threading.Thread(target=spread_data)
            t.start()
            t.join()

            break
        else:
            t = threading.Thread(target=spread_data)
            t.start()
            t.join()

while True:
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)

    clients.append(tcpCliSock)
    th = threading.Thread(target=handle_request)
    th.start()
    #th.join()


tcpSerSock.close()
