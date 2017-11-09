import RPi.GPIO as GPIO
from time import sleep
import socket
import os

rood = 21 #GPIO port 21
geel = 24 #GPIO port 24
groen = 25 #GPIO port 25
button1 = 18 #GPIO port 18
button2 = 23 #GPIO port 23
buz = 16 #GPIO port 16
host = input("Wat is het IP van de server? Voorbeeld: 192.168.3.139 ")
#Variabelen aanmaken

def init():
    GPIO.output(groen, True) #Groene lampje wordt aangezet
    GPIO.output(rood, False) #Rode lampje wordt aangezet
    GPIO.output(geel, False) #Gele lampje wordt aangezet
    alarm()
    #GPIO initialiseren

def alarm():
    while True:
        host_online = os.system("ping -c 1 " + str(host))  # Kijken of host online is.
        if host_online == 0:
            i = 0 #Telwaarde definieren
            aftellen = 10 #Tellen tot waarde in deze variabele
            afgeteld = 0 #Waarde om check mee te doen

            if GPIO.input(button1) == GPIO.HIGH: #Kijk of button 1 ingedrukt is
                if afgeteld == 0:  # Kijken of alarm getriggerd is
                    GPIO.output(geel, True) #Zet geel aan
                    GPIO.output(groen, False) #Zet groen uit
                    # Het gele lampje gaat aan en de groene uit

                    while i < aftellen:  # Aftellen voordat alarm initieerd
                        i = i + 1
                        sleep(1) #Wacht 1 seconde
                        print("Nog " + str(aftellen - i) + " seconden voordat alarm afgaat!")
                        if GPIO.input(button2) == GPIO.HIGH: #Stop met aftellen wanneer knop 2 is ingedrukt
                            break

                    if i == aftellen:  # Als afgeteld is wordt deze code uitgevoerd
                        GPIO.output(rood, True) #Rood aan
                        GPIO.output(geel, False) #Geel uit
                        GPIO.output(groen, False) #Groen uit
                        # Het rode lampje gaat aan en de andere uit.
                        stuur_bericht("1")  # Stuur bericht naar server.
                        while True: #Buzzer loop
                            GPIO.output(buz, True)
                            sleep(0.001)
                            GPIO.output(buz, False)
                            sleep(0.001)
                            if GPIO.input(button2) == GPIO.HIGH: #Alarm afzetten
                                print("Alarm is afgezet")
                                break
                        init() #Alarm opnieuw starten
                    else:
                        GPIO.output(rood, False)
                        GPIO.output(geel, False)
                        GPIO.output(groen, True)
                        # Als niet afgeteld is naar standaard lampen code
                else:
                    print("Alarm is al ingezet")
                    sleep(1)
        else:
            GPIO.output(rood, True)  # Rode lampje aan
            GPIO.output(geel, False)  # Gele lampje uit
            GPIO.output(groen, False)  # Groene lampje uit
            # Het rode lampje gaat aan en de andere uit.
            stuur_bericht("1")  # Stuur bericht naar server.
            while True:  # Buzzer loop
                GPIO.output(buz, True)
                sleep(0.001)
                GPIO.output(buz, False)
                sleep(0.001)
                if GPIO.input(button2) == GPIO.HIGH:  # Alarm afzetten
                    print("Alarm is afgezet")
                    break
            init()  # Alarm opnieuw starten

def stuur_bericht(bericht):
    s = socket.socket()  # Socket aanmaken
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Laat het programma de port en adres hergebruiken wanneer socket gesloten is
    s.bind(('', 12347)) #Bind naar alle adressen die client te bieden heeft met port 12347
    s.listen(5)  # Luister naar alle adressen die de raspberry heeft
    #Wachten tot de server het bericht opvangt
    print("Bericht versturen...")
    while True:
        c, addr = s.accept() #Accepteer alle verbindingen
        print('Server: ' + addr[0] + " heeft het bericht ontvangen")
        c.send(bericht)
        c.close()#Sluit verbinding met client en sluit socket zodat port en adres weer gebruikt kunnen worden
        s.close()
        break

GPIO.setwarnings(False) #GPIO
GPIO.setmode(GPIO.BCM) #GPIO BCM mode (GPIO layout)
GPIO.setup(buz, GPIO.OUT) #Buzzer die afgaat wanneer alarm afgaat
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button die alarm triggert, oftewel de deur gaat open.
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button die alarm uitzet.
GPIO.setup(rood, GPIO.OUT) #Het rode lampje
GPIO.setup(geel, GPIO.OUT) #Het gele lampje
GPIO.setup(groen, GPIO.OUT) #Het groene lampje

init() #Start alarm