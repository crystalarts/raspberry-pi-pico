import machine
import network
import utime

ssid = "name"
password = "password"

print("┏╋━━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━━╋┓")
print("  \033[94;1mWi-Fi connection and range strength\033[0m")
print("           \033[94;1mRaspberry Pi Pico\033[0m")
print("┗╋━━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━━╋┛")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('\033[95m[I]\033[0m \033[91mWaiting for connection...\033[0m')
        utime.sleep(5)
ip = wlan.ifconfig()[0]

wifi_strength = wlan.status("rssi")
mapped_strength = int((wifi_strength + 100) * 4 / 60)

strength = ""
if mapped_strength == 1:
    strength = "Wi-Fi coverage strength \033[91m:\033[0m \033[93m1 line"
if mapped_strength == 2:
    strength = "Wi-Fi coverage strength \033[91m:\033[0m \033[93m2 lines"
if mapped_strength == 3:
    strength = "Wi-Fi coverage strength \033[91m:\033[0m \033[93m3 lines"
if mapped_strength == 4:
    strength = "Wi-Fi coverage strength \033[91m:\033[0m \033[93m4 lines"

print("")
print(f"\033[95m[I]\033[0m \033[91m»\033[0m Connected to the network \033[91m:\033[0m \033[93m{ssid}")
print(f"\033[95m[I]\033[0m \033[91m»\033[0m IP address obtained \033[91m:\033[0m \033[93m{ip}")
print("\033[95m[I]\033[0m \033[91m»\033[0m", strength)
print("")
