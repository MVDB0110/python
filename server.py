import socket
import json
from time import sleep

host = 'raspbian_mike'

def ontvangen():
    try:
        s = socket.socket()
        s.connect((host, 12345))
        s.close
        return s.recv(1024)

    except:
        return '0'
        sleep(15)

print(json.dumps(ontvangen()))