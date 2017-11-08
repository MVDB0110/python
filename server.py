import socket
import json
from time import sleep

host = 'raspbian_mike'

def ontvangen():
    try:
        s = socket.socket()
        s.connect((host, 12345))
        s.close
        return s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft.

    except:
        return '0'

print(json.dumps(ontvangen()))