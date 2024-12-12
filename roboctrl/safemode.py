#!/usr/bin/python3
import libctrl.ctrl as ctrl
import sys
from time import sleep
from autodrive import reactoprx as divert


risk = float(0.0)
safedist = sys.argv[1]
spd = 30
pspd = 25
tspd = 30
dtime = 0.420
tof = ctrl.get_stat.measure_dist(5)
bumper = ctrl.get_stat.get_bumper()


def safemode(spd, pspd):
    while True:
        sleep(0.1)
        if any(bumper) or (tof <= safedist):
            divert(spd, pspd)
