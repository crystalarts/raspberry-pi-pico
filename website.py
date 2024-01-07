import network
import socket
import utime

print("┏╋━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━╋┓")
print("       \033[94;1m● Raspberry Pi Pico ●\033[0m")
print("         \033[94;1m● Website Create ●\033[0m")
print("┗╋━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━╋┛")
print("")

ssid = "name"
password = "password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('\033[95m[I]\033[0m » \033[92mWaiting for connection...\033[0m')
        utime.sleep(5)
ip = wlan.ifconfig()[0]
print(f'\033[95m[I]\033[0m » \033[92mConnected to WiFi:\033[0m \033[93m{ip}\033[0m')

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print(f'\033[95m[I]\033[0m » \033[92mWebsite launched on\033[0m \033[93m{ip}:{addr[1]}\033[0m')

html = f'''
<!DOCTYPE html>
<html>
    <head>
        <title>Pico W</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta charset="UTF-8">
    </head>
    <body style='background-color: #E4E8EB; margin: 0; padding: 0;'>
        <h1>Hello World</h1>
    </body>
</html>
'''

try:
    while True:
        cl, addr = s.accept()
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()
except KeyboardInterrupt:
    s.close()
    wlan.disconnect()
    wlan.active(False)
    print('\033[95m[I]\033[0m » \033[91mServer terminated.\033[0m')
