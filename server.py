import socket
import threading
from tkinter import *
from time import sleep

root = Tk()
root.title("Dashboard")

host = 'raspbian_mike'
var = StringVar()

def knop_gedrukt():
    threadontvang.start()
    button.pack_forget()

def ontvangen():
    try:
        s = socket.socket()
        s.connect((host, 12345))
        s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft.
        s.close()
        var.set("Alarm gaat af op client.")
        print("Alarm gaat af op client.")
        threadontvang.cancel()
        button.pack()

    except:
        var.set("Alarm gaat niet af op client.")
        print("Alarm gaat niet af op client.")

threadontvang = threading.Timer(15.0, ontvangen)
threadontvang.start()

button = Button(root, text="Alarm is afgezet.", command=knop_gedrukt)
text = Label(root, textvariable=var)
text.pack()

root.mainloop()