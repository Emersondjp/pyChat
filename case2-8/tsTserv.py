#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################################
## Description :
##   使用fork实现全双工聊天程序。服务器端，主进程处理接受，子进程处理发送。
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

pid = os.fork()
if pid == 0 :  # 子进程
    while True:
        data = input('>')
        if not data:
            tcpCliSock.send('')
            break
        else:
            msg = "[{host}@{time}] {data}".format(host=os.name, time=ctime(), data=data)
            tcpCliSock.send(msg.encode())
else : # 父进程
    while True:
        data = tcpCliSock.recv(1024)
        if not data:
            break
        else:
            print(data.decode())

tcpCliSock.close()

tcpSerSock.close()
