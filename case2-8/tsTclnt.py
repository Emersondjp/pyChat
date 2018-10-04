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
from time import ctime
import os

HOST = args.serv
PORT = eval(args.port)
#HOST = 'localhost'
#PORT = 21567
BUFSIZ = 1024
ADDR = ( HOST, PORT )

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect( ADDR )

pid = os.fork()

if pid == 0: #子进程处理接受
    while True:
        data = tcpCliSock.recv(1024)
        if not data:
            break
        else:
            print(data.decode())
else: #父进程处理发送
    while True:
        data = input('>')
        if not data:
            break
        else:
            msg = "[{host}@{time}] {data}".format(host=os.name, time=ctime(), data=data)
            tcpCliSock.send(msg.encode())

tcpCliSock.close()
