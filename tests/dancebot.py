#!/usr/bin/python3
import roboctrl.libctrl.ctrl as ctrl
from time import sleep

spd = 17
tspd = 20
pspd = 10


for i in range(1):
    ctrl.drive_forward(spd, pspd)
    sleep(1)
    ctrl.drive_backward(spd, pspd)
    sleep(0.5)
    ctrl.drive_fwleft(spd, pspd, tspd)
    sleep(0.25)
    ctrl.drive_fwright(spd, pspd, tspd)
    sleep(0.25)
    ctrl.full_stop()
    sleep(0.2)
    ctrl.drive_backward(pspd, tspd)
    sleep(0.75)
    ctrl.turn_left(pspd, tspd)
    sleep(1)
    ctrl.full_stop()
    sleep(0.009)
    ctrl.turn_right(pspd, tspd)
    sleep(1)
    ctrl.full_stop()
    sleep(0.009)

