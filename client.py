import RPi.GPIO as GPIO
from time import sleep
import socket
import threading

rood = 21
geel = 24
groen = 25
button1 = 18
button2 = 23
buz = 16
#Variabelen aanmaken

def init():
    GPIO.output(groen, True) #Groene lampje wordt aangezet
    GPIO.output(rood, False) #Rode lampje wordt aangezet
    GPIO.output(geel, False) #Gele lampje wordt aangezet
    alarm()
    #GPIO initialiseren

def alarm():
    while True:
        i = 0
        aftellen = 10
        afgeteld = 0
        if GPIO.input(button1) == GPIO.HIGH:
            if afgeteld == 0:  # Kijken of alarm getriggerd is
                GPIO.output(geel, True)
                GPIO.output(groen, False)
                # Het gele lampje gaat aan en de groene uit

                while i < aftellen:  # Aftellen voordat alarm initieerd
                    i = i + 1
                    sleep(1)
                    print("Nog " + str(aftellen - i) + " seconden voordat alarm afgaat!")
                    if GPIO.input(button2) == GPIO.HIGH:
                        break

                if i == aftellen:  # Als afgeteld is wordt deze code uitgevoerd
                    afgeteld = 1
                    GPIO.output(rood, True)
                    GPIO.output(geel, False)
                    GPIO.output(groen, False)
                    # Het rode lampje gaat aan en de andere uit.
                    stuur_bericht("1")  # Stuur bericht naar server.
                    while True:
                        GPIO.output(buz, True)
                        sleep(0.001)
                        GPIO.output(buz, False)
                        sleep(0.001)
                        if GPIO.input(button2) == GPIO.HIGH:
                            print("Alarm is afgezet")
                            break
                    init()
                else:
                    GPIO.output(rood, False)
                    GPIO.output(geel, False)
                    GPIO.output(groen, True)
                    # Als niet afgeteld is naar standaard lampen code
            else:
                print("Alarm is al ingezet")
                sleep(1)

        if GPIO.input(button2) == GPIO.HIGH:
            if i == aftellen:
                print("Alarm kan niet afgezet worden!")
                sleep(1)

def stuur_bericht(bericht):
    s = socket.socket()  # Socket aanmaken
    s.bind(('', 12345))
    s.listen(5)  # Luister naar alle adressen die de raspberry heeft
    #Wachten tot de server het bericht opvangt
    while True:
        try:
            c, addr = s.accept() #Accepteer alle verbindingen
            print('Ik heb verbinding met: ', addr)
            c.send(bericht)
            c.close()
            break
        except:
            print("Bericht kan nog niet verstuurd worden.")
            sleep(1)

GPIO.setwarnings(False) #GPIO
GPIO.setmode(GPIO.BCM) #GPIO BCM mode (GPIO layout)
GPIO.setup(buz, GPIO.OUT) #Buzzer die afgaat wanneer alarm afgaat
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button die alarm triggert, oftewel de deur gaat open.
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button die alarm uitzet.
GPIO.setup(rood, GPIO.OUT) #Het rode lampje
GPIO.setup(geel, GPIO.OUT) #Het gele lampje
GPIO.setup(groen, GPIO.OUT) #Het groene lampje
init()