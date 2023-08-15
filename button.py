from machine import Pin
from utime import sleep

button1 = Pin(0, Pin.IN)

while True:
    if button1.value() == 1:
        print("Naciśnięto przycisk")
    sleep(0.3)