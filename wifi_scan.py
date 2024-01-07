import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wifi_strength = wlan.status("rssi")
mapped_strength = int((wifi_strength + 100) * 4 / 60)

strength = ""
if mapped_strength == 1:
    strength = "1 line"
if mapped_strength == 2:
    strength = "2 lines"
if mapped_strength == 3:
    strength = "3 lines"
if mapped_strength == 4:
    strength = "4 lines"

networks = wlan.scan()
print("┏╋━━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━━╋┓")
print("      \033[94;1mWi-Fi connections available\033[0m")
print(" \033[94;1mAvailable Wi-Fi networks in the area\033[0m")
print("         \033[94;1mCheck if it's yours\033[0m")
print("┗╋━━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━━╋┛")
print("")

for net in networks:
    ssid = net[0].decode("utf-8")
    rssi = net[3]
    print("\033[95m[I]\033[0m \033[91m»\033[0m SSID:\033[93m", ssid, "\033[0m\033[91m»\033[0m RSSI:\033[93m", rssi, "\033[0m\033[91m»\033[0m STRONG:\033[93m", strength, "\033[0m")
