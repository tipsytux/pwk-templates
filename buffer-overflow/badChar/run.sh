#!/bin/bash

cat hexDump | cut -d " " -f 3,4,5,6,7,8,9,10 | sed ':a;N;$!ba;s/\n/ /g' > check_space
./identify.py
