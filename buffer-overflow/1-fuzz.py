#!/usr/bin/python
import sys,socket
from time import sleep
from machineConstants import *
buffer = "A" * 100
while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((targetIP,port))
        s.settimeout(5)
        s.send((command + buffer))
        print ("Fuzzing with %s bytes" % len(buffer))
        s.recv(1024)
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print "Fuzzing crashed at %s bytes" % str(len(buffer))
        sys.exit()
