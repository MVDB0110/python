import socket
import threading
from tkinter import *

root = Tk() #'Master' window
root.title("Dashboard") #Titel van window

host = "192.168.3.241" #IP adres van client (Dit is variabel tenzij er een static ip aangegeven is)

def knop_gedrukt():
    ontvangen() #Ontvangen initieren
    button.pack_forget() #Button weghalen
    #Standaard situatie herstellen

def ontvangen():
    try:
        s = socket.socket() #Maak socket
        s.connect((socket.gethostbyname(host), 12347)) #Verbind met client
        s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft
        s.close() #Sluit socket
        var.set("Alarm gaat af op client.") #Pas text aan op GUI
        print("Alarm gaat af op client.") #Print text in console
        button.pack() #Laat button (weer) verschijnen

    except:
        var.set("Alarm gaat niet af op client.") #Pas text aan op GUI
        print("Alarm gaat niet af op client.") #Print text in console
        threading.Timer(5.0, ontvangen).start() #Start timer op ontvangen()

button = Button(root, text="Alarm is afgezet.", command=knop_gedrukt) #Button definieren
var = StringVar() #Statement van variabele text in Label
var.set("Alarm gaat niet af op client.") #Pas text aan op GUI
text = Label(root, textvariable=var) #Definieer Label
text.pack() #Laat text verschijnen

ontvangen() #Start ontvangen eerste keer
root.mainloop() #Open window met tkinter