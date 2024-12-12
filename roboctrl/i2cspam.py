#!/usr/bin/python3
import time
import libctrl.ctrl as ctrl 
import timeit
def spam_iic():
    stime = 0.01
    while True:
        ctrl.full_stop()
        time.sleep(stime)

def spam_better():
    timeit.timeit(spam_iic(), number=100)
