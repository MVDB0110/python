import socket
from time import sleep

def ontvangen():
    while True:
        try:
            s = socket.socket()
            s.connect(('192.168.42.1', 12345))
            s.close
            return s.recv(1024)
            break
        except:
            print('Geen alarmcode ontvangen.')
            sleep(15)

print(ontvangen())