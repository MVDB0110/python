import socket
from time import sleep

def ontvangen():
    while True:
        try:
            s = socket.socket()
            s.connect(('localhost', 12345))
            s.close
            return s.recv(1024)
        except:
            print('Geen alarmcode ontvangen.')
            sleep(45)
            return 0