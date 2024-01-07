import machine
from machine import Pin
import gc

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
readings = sensor_temp.read_u16() * conversion_factor
        
temperature = 27 - (readings - 0.706) / 0.001721
free_memory = gc.mem_free() / 1024
allocated_memory = gc.mem_alloc() / 1024
total_memory = (gc.mem_free() + gc.mem_alloc()) / 1024

memory_usage_percentage = (1 - (free_memory / total_memory)) * 100

temp = ""
if temperature > 0:
    temp = "\033[95m[I]\033[0m \033[91m»\033[0m \033[36mTemperature\033[0m: \033[32m{:.2f}\033[0m °C".format(temperature)
if temperature > 45:
    temp = "\033[95m[I]\033[0m \033[91m»\033[0m \033[36mTemperature\033[0m: \033[33m{:.2f}\033[0m °C".format(temperature)
if temperature > 75:
    temp = "\033[95m[I]\033[0m \033[91m»\033[0m \033[36mTemperature\033[0m: \033[31m{:.2f}\033[0m °C".format(temperature)

print("")
print("┏╋━━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━━╋┓")
print("   \033[33mCPU temperature and memory usage\033[0m")
print("          \033[33mRaspberry Pi Pico\033[0m")
print("┗╋━━━━━━━ ◥◣ ◆ ◢◤ ━━━━━━━╋┛")
print("")
print(temp)
print("\033[95m[I]\033[0m \033[91m»\033[0m \033[36mMemory usage\033[0m: \033[93m{:.2f}\033[0m kB".format(allocated_memory))
print("\033[95m[I]\033[0m \033[91m»\033[0m \033[36mFree memory\033[0m: \033[93m{:.2f}\033[0m kB".format(free_memory))
print("\033[95m[I]\033[0m \033[91m»\033[0m \033[36mTotal memory\033[0m: \033[93m{:.2f}\033[0m kB".format(total_memory))
print("\033[95m[I]\033[0m \033[91m»\033[0m \033[36mMemory usage percentage\033[0m: \033[93m{:.2f}\033[0m%".format(memory_usage_percentage))
print("")
