import socket
import threading
from tkinter import *

root = Tk() #'Master' window
root.title("Dashboard") #Titel van window

host = "raspbianmbrink.local" #Hostname van client.
portnummer = 12347 #Port waarop verbonden gaat worden

threadcycle = 5.0 #Deze variabele laat om de aangegeven seconden de thread weer opstarten

var = StringVar() #Statement van variabele text in Label
var.set("Alarm gaat niet af op client.") #Pas text aan op GUI

def knop_gedrukt():
    ontvangen() #Ontvangen initieren
    button.pack_forget() #Button weghalen
    #Standaard situatie herstellen

def ontvangen():
    try:
        s = socket.socket() #Maak socket
        s.connect((socket.gethostbyname(host), portnummer)) #Verbind met client
        s.recv(1024)#Return waarde 1 wanneer socket verbinding heeft
        s.close() #Sluit socket
        var.set("Alarm gaat af op client.") #Pas text aan op GUI
        print("Alarm gaat af op client.") #Print text in console
        button.pack() #Laat button (weer) verschijnen

    except:
        var.set("Alarm gaat niet af op client.") #Pas text aan op GUI
        print("Alarm gaat niet af op client.") #Print text in console
        threading.Timer(threadcycle, ontvangen).start() #Start timer op ontvangen()

text = Label(root, textvariable=var) #Definieer Label
button = Button(root, text="Alarm is afgezet.", command=knop_gedrukt) #Button definieren
text.pack() #Laat text verschijnen

ontvangen() #Start ontvangen eerste keer
root.mainloop() #Open window met tkinter