#!/usr/bin/python3
from roboctrl.libctrl.i2cwrapper import get_bat_voltage as getvolt
import time

f = open("battdischcurve.txt", 'w')
batt = getvolt()
x = 0
if x <= 10000:
    x = x + 1
    f.write("Time: ", time.time,"Voltage: ",  batt, "V")
    print("Time: ", time.time,"Voltage: ",  batt, "V")
    time.sleep(10)

