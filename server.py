import socket
import threading
from tkinter import *
from time import sleep

root = Tk()
root.title("Dashboard")

host = '192.168.3.241'
var = StringVar()

def knop_gedrukt():
    ontvangen()
    button.pack_forget()

def ontvangen():
    try:
        s = socket.socket()
        s.connect((host, 12345))
        s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft.
        s.close()
        var.set("Alarm gaat af op client.")
        print("Alarm gaat af op client.")
        button.pack()

    except:
        var.set("Alarm gaat niet af op client.")
        print("Alarm gaat niet af op client.")
        threading.Timer(15.0, ontvangen).start()

var.set("Alarm gaat niet af op client.")

button = Button(root, text="Alarm is afgezet.", command=knop_gedrukt)
text = Label(root, textvariable=var)
text.pack()

ontvangen()
root.mainloop()