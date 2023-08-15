import machine
from machine import Pin
from dht import DHT11, InvalidChecksum

pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

temp = ""
if sensor.temperature < 10:
   temp = "   ・Temperatura: {}°C".format(sensor.temperature) + " ( Zimno ) "
if sensor.temperature >= 10 and sensor.temperature < 25:
    temp = "   ・Temperatura: {}°C".format(sensor.temperature) + " ( Chłodno ) "
if sensor.temperature >= 25 and sensor.temperature < 35:
    temp = "   ・Temperatura: {}°C".format(sensor.temperature) + " ( Ciepło ) "
if sensor.temperature > 35:
    temp = " ・Temperatura: {}°C".format(sensor.temperature) + " ( Gorąco ) "

humi = ""
if sensor.humidity < 30:
    humi = "    ・Wilgotność: {}%".format(sensor.humidity) + " ( Niska ) "
if sensor.humidity >= 30 and sensor.humidity < 60:
    humi = "  ・Wilgotność: {}%".format(sensor.humidity) + " ( Umiarkowana ) "
if sensor.humidity >= 60 and sensor.humidity < 80:
    humi = "    ・Wilgotność: {}%".format(sensor.humidity) + " ( Wysoka ) "
if sensor.humidity > 80:
    humi = " ・Wilgotność: {}%".format(sensor.humidity) + " ( Bardzo wysoka ) "

print("")
print("")
print("")
print("       Temperatura i wilgotność")
print("    Raspberry Pi Pico WH && DHT11")
print("--------------------------------------")
print(temp)
print(humi)
print("")
print("")