import socket
import threading
from tkinter import *
from time import sleep

root = Tk()
root.title("Dashboard")

host = '192.168.3.241'

def knop_gedrukt():
    ontvangen()
    button.pack_forget()

def ontvangen():
    try:
        s = socket.socket()
        s.connect((socket.gethostbyname(host), 12347))
        s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft.
        s.close()
        var.set("Alarm gaat af op client.")
        print("Alarm gaat af op client.")
        button.pack()

    except:
        var.set("Alarm gaat niet af op client.")
        print("Alarm gaat niet af op client.")
        threading.Timer(15.0, ontvangen).start()

button = Button(root, text="Alarm is afgezet.", command=knop_gedrukt)
var = StringVar()
var.set("Alarm gaat niet af op client.")
text = Label(root, textvariable=var)
text.pack()

ontvangen()
root.mainloop()