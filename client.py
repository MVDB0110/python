import RPi.GPIO as GPIO
from time import sleep
import socket

def stuur_bericht(bericht):
    while True:
        c, addr = s.accept()
        print('Ik heb verbinding met: ', addr)
        c.send(bericht)
        c.close()
        break

s = socket.socket()
s.bind(('', 12345))
s.listen(5)

rood = 21
geel = 24
groen = 25
button1 = 18
button2 = 23
buz = 16
afgeteld = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buz, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rood, GPIO.OUT)
GPIO.setup(geel, GPIO.OUT)
GPIO.setup(groen, GPIO.OUT)
GPIO.output(groen, True)
GPIO.output(rood, False)
GPIO.output(geel, False)

while True:
    if GPIO.input(button1) == GPIO.HIGH:
        i = 0
        aftellen = 10
        if afgeteld == 0:
            GPIO.output(geel, True)
            GPIO.output(groen, False)
            GPIO.output(rood, False)

            while i < aftellen:
                i = i + 1
                sleep(1)
                print("Nog " + str(aftellen - i) + " seconden voordat alarm afgaat!")
                if GPIO.input(button2) == GPIO.HIGH:
                    break

            if i == aftellen:
                afgeteld = 1
                GPIO.output(rood, True)
                GPIO.output(geel, False)
                GPIO.output(groen, False)
                stuur_bericht("1")
                while True:
                    GPIO.output(buz, True)
                    sleep(0.001)
                    GPIO.output(buz, False)
                    sleep(0.001)
                    if GPIO.input(button2) == GPIO.HIGH:
                        break

            else:
                GPIO.output(rood, False)
                GPIO.output(geel, False)
                GPIO.output(groen, True)
        else:
            print("Alarm is al ingezet")
            sleep(1)

    if GPIO.input(button2) == GPIO.HIGH:
        if i == aftellen:
            print("Alarm kan niet afgezet worden!")
            sleep(1)
