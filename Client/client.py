import RPi.GPIO as GPIO
from time import sleep

rood = 21
geel = 24
groen = 25
button1 = 18
button2 = 23
buz = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buz, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rood, GPIO.OUT)
GPIO.setup(geel, GPIO.OUT)
GPIO.setup(groen, GPIO.OUT)
GPIO.output(groen, True)
while True:
    i = 0
    aftellen = 10
    if GPIO.input(button1) == GPIO.HIGH:
        GPIO.output(geel, True)
        while i < aftellen:
            i = i + 1
            sleep(1)
            print("Nog " + str(aftellen - i) + " seconden voordat alarm afgaat!")
            if GPIO.input(button2) == GPIO.HIGH:
                break
    GPIO.output(rood, True)
    GPIO.output(groen, False)
    while True:
        GPIO.output(buz, True)
        sleep(0.001)
        GPIO.output(buz, False)
        sleep(0.001)
        if GPIO.input(button2) == GPIO.HIGH:
            break
    if GPIO.input(button2) == GPIO.HIGH:
        if i == aftellen:
            print("Alarm kan niet afgezet worden!")
        else:
            GPIO.output(groen, True)
            GPIO.output(rood, False)
            GPIO.output(buz, False)
