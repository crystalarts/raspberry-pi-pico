from machine import Pin
import utime
pir = Pin(28, Pin.IN)
led = Pin(15, Pin.OUT)
led.low()
while True:
    if pir.value() == 1:
        led.high()
        utime.sleep(5)
    else:
        led.low()
utime.sleep(0.2)