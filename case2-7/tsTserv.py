#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################################
## Description :
##
##
## Usage :
##
##
## Mentioin :
##
##
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

HOST = args.serv
PORT = eval(args.port)
BUFSIZ = 2014
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

print('warting for connection...')
tcpCliSock, addr = tcpSerSock.accept()
print('...connected from: ', addr)

while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print("[%s@%s] %s" % (addr, ctime(), data.decode()))
    data = input('>')
    tcpCliSock.send(data.encode())
    if not data:
        break

tcpCliSock.close()

tcpSerSock.close()
