#!/usr/bin/env python3
import os
import platform
import time

statsos = str(platform.system())
cpuusage=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))


keyboard.send_keys("OS: " "Ubuntu " + statsos + " 17.04")
keyboard.send_keys("<shift>+<enter>")
keyboard.send_keys("CPU:  " + cpuusage + "%" + " -  Intel® Core™ i5-3570K CPU @ 3.40GHz × 4 ")
keyboard.send_keys("<shift>+<enter>")
keyboard.send_keys("Graphics : GeForce GTX 760/PCIe/SSE2")
keyboard.send_keys("<shift>+<enter>")
time.sleep(1.0)
keyboard.send_keys("Total ram : 8.0gbs")
time.sleep(6.0)
keyboard.send_keys("<enter>")
