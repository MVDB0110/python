import socket
import threading
from tkinter import *
from time import sleep

host = 'raspbian_mike'

root = Tk()
root.title("Dashboard")
var = StringVar()

def init():
    text = Label(root, textvariable=var)
    text.pack()

def ontvangen():
    threading.Timer(15.0, ontvangen).start()
    try:
        s = socket.socket()
        s.connect((host, 12345))
        s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft.
        s.close()
        var.set("Alarm gaat af op client.")
        print("Alarm gaat af op client.")

    except:
        var.set("Alarm gaat niet af op client.")
        print("Alarm gaat niet af op client.")

ontvangen()
init()
root.mainloop()