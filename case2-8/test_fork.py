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

#################### Begin Argument Parser #########################
#import argparse
#parser = argparse.ArgumentParser(description="your script description")
#parser.add_argument('-i', '--input',  dest='inp', action='store', default='inp', help='input')
#parser.add_argument('-o', '--output', dest='out', action='store', default='out', help='output')
#
#args = parser.parse_args()
#
#print(args)
##################### End Argument Parser ##########################
#
import os
pid = os.fork()
if pid == 0:
    print("this is sub process. pid is {pid}.".format_map(locals()))
else:
    print("this is father process. sub-pid is {pid}.".format_map(locals()))

print("Will this sentance excute twice?")

