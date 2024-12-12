#!/usr/bin/python3

#import serial
import PyLidar3
import time
#ser = serial.Serial('/dev/ttyS0')
#ser_bytes = ser.readline()

device = '/dev/ttyS0'
baudRate = 115200
Obj = PyLidar3.YdLidarG4(device)


