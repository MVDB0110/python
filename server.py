import socket
import threading
from tkinter import *
from time import sleep

host = 'raspbian_mike'

root = Tk()
root.title("Dashboard")
var = StringVar()

def stuur_bericht(bericht):
    s = socket.socket()  # Socket aanmaken
    s.bind(('', 12345))
    s.listen(5)  # Luister naar alle adressen die de raspberry heeft
    #Wachten tot de server het bericht opvangt
    while True:
        c, addr = s.accept() #Accepteer alle verbindingen
        print('Ik heb verbinding met: ', addr)
        c.send(bericht)
        c.close()
        break

def init():
    text = Label(root, textvariable=var)
    text.pack()
    uitzetten = Button(root, text='Alarm afzetten', command=lambda: stuur_bericht("1"))
    uitzetten.pack()

def ontvangen():
    threading.Timer(15.0, ontvangen).start()
    try:
        s = socket.socket()
        s.connect((host, 12345))
        s.close()
        s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft.
        var.set("Alarm gaat af op client.")
        print("Alarm gaat af op client.")

    except:
        var.set("Alarm gaat niet af op client.")
        print("Alarm gaat niet af op client.")

ontvangen()
init()
root.mainloop()