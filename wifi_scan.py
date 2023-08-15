import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wifi_strength = wlan.status("rssi")
mapped_strength = int((wifi_strength + 100) * 4 / 60)

strength = ""
if mapped_strength == 1:
    strength = "1 kreska"
if mapped_strength == 2:
    strength = "2 kreski"
if mapped_strength == 3:
    strength = "3 kreski"
if mapped_strength == 4:
    strength = "4 kreski"

networks = wlan.scan()
print("")
print("")
print("")
print("       Dostępne połączenia Wi-Fi")
print("          Raspberry Pi Pico W")
print("--------------------------------------")
print("    Dostępne sieci Wi-Fi w okolicy:")
print("        Sprawdź czy jest twoje:")
print("")

for net in networks:
    ssid = net[0].decode("utf-8")
    rssi = net[3]
    print("SSID:", ssid, "| RSSI:", rssi, "| Siła:", strength)

time.sleep(10)