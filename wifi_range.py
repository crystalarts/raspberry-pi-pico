import machine
from machine import Pin
import network

led = Pin("LED", Pin.OUT)

ssid = "podaj nazwę sieci"
password = "podaj hasło sieci"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Oczekiwanie na połączenie...')
        utime.sleep(5)
ip = wlan.ifconfig()[0]
print(f'Połączono z WiFi: {ip}')
led.on()

wifi_strength = wlan.status("rssi")
mapped_strength = int((wifi_strength + 100) * 4 / 60)

strength = ""
if mapped_strength == 1:
    strength = "      Siła zasięgu : | (1 kreska)"
if mapped_strength == 2:
    strength = "     Siła zasięgu : || (2 kreski)"
if mapped_strength == 3:
    strength = "     Siła zasięgu : ||| (3 kreski)"
if mapped_strength == 4:
    strength = "     Siła zasięgu : |||| (4 kreski)"

print("")
print("")
print("")
print("    Połączenie wifi i siła zasięgu")
print("         Raspberry Pi Pico WH")
print("--------------------------------------")
print(f"    Połączono z siecią : {ssid}")
print(f"       Adres IP : {ip}")
print(strength)
print("")