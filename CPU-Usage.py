#!/usr/bin/env python3
import os
import platform
import time
cpuusage=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))



keyboard.send_keys("CPU:  " + cpuusage + "%" + " | Current temp: 0*c!")
keyboard.send_keys("<enter>")
#Adding temp as i figure out an native python 2.6+ way to get it!
