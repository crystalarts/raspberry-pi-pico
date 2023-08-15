import machine
from machine import Pin
import gc

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
readings = sensor_temp.read_u16() * conversion_factor
        
temperature = 27 - (readings - 0.706) / 0.001721
free_memory = gc.mem_free() / 1024
allocated_memory = gc.mem_alloc() / 1024

print("")
print("")
print("")
print("  Temperatura CPU i zużycie pamięci")
print("        Raspberry Pi Pico WH")
print("-------------------------------------")
print("      ・Temperatura: {:.2f} °C".format(temperature))
print(" ・Zużycie pamięci: {:.2f}".format(allocated_memory) + " / " + "{:.2f} kB".format(free_memory))
print("")
print("")