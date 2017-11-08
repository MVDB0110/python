import socket
import json
from time import sleep

host = 'raspbian_mike'

def ontvangen():
    while True:
        try:
            s = socket.socket()
            s.connect((host, 12345))
            s.close
            return s.recv(1024)
            break
        except:
            print('Geen alarmcode ontvangen.')
            sleep(15)

print(json.dumps(ontvangen()))