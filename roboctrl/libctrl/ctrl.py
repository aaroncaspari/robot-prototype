#!/usr/bin/python3
# Copyright (C) Aaron Caspri 2022
import libctrl.i2cwrapper as i2cw
from time import sleep
from statistics import median
ptime = float(0.1)


class drive():

    def drive_fw_nps(spd):
        i2cw.direc1 = i2cw.DIRECTION_FORWARD
        i2cw.direc2 = i2cw.DIRECTION_FORWARD
        i2cw.speed1 = spd
        i2cw.speed2 = spd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_forward(spd, pspd):
        i2cw.direc1 = i2cw.DIRECTION_FORWARD
        i2cw.direc2 = i2cw.DIRECTION_FORWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = spd
        i2cw.speed2 = spd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_backward(spd, pspd):
        i2cw.direc1 = i2cw.DIRECTION_BACKWARD
        i2cw.direc2 = i2cw.DIRECTION_BACKWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = int(float(spd/1.25))
        i2cw.speed2 = int(float(spd/1.25))
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def turn_left(pspd, tspd):
        i2cw.direc1 = i2cw.DIRECTION_BACKWARD
        i2cw.direc2 = i2cw.DIRECTION_FORWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = tspd
        i2cw.speed2 = tspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def turn_right(pspd, tspd):
        i2cw.direc1 = i2cw.DIRECTION_FORWARD
        i2cw.direc2 = i2cw.DIRECTION_BACKWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = tspd
        i2cw.speed2 = tspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_fwleft(spd, pspd, tspd):
        i2cw.direc1 = i2cw.DIRECTION_FORWARD
        i2cw.direc2 = i2cw.DIRECTION_FORWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = tspd
        i2cw.speed2 = spd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_fwleftrad(spd, pspd, rad):
        tspd = int(spd/rad)
        i2cw.direc1 = i2cw.DIRECTION_FORWARD
        i2cw.direc2 = i2cw.DIRECTION_FORWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = tspd
        i2cw.speed2 = spd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_fwright(spd, pspd, tspd):
        i2cw.direc1 = i2cw.DIRECTION_FORWARD
        i2cw.direc2 = i2cw.DIRECTION_FORWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = spd
        i2cw.speed2 = tspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_fwrightrad(spd, pspd, rad):
        tspd = int(spd/rad)
        i2cw.direc1 = i2cw.DIRECTION_FORWARD
        i2cw.direc2 = i2cw.DIRECTION_FORWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = spd
        i2cw.speed2 = tspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_bwleft(spd, pspd, tspd):
        i2cw.direc1 = i2cw.DIRECTION_BACKWARD
        i2cw.direc2 = i2cw.DIRECTION_BACKWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = int(float(tspd/1.25))
        i2cw.speed2 = int(float(spd/1.25))
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_bwleftrad(spd, pspd, rad):
        tspd = int(spd/rad)
        i2cw.direc1 = i2cw.DIRECTION_BACKWARD
        i2cw.direc2 = i2cw.DIRECTION_BACKWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = int(float(tspd/1.25))
        i2cw.speed2 = int(float(spd/1.25))
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_bwright(spd, pspd, tspd):
        i2cw.direc1 = i2cw.DIRECTION_BACKWARD
        i2cw.direc2 = i2cw.DIRECTION_BACKWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = int(float(spd/1.25))
        i2cw.speed2 = int(float(tspd/1.25))
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def drive_bwrightrad(spd, pspd, rad):
        tspd = int(spd/rad)
        i2cw.direc1 = i2cw.DIRECTION_BACKWARD
        i2cw.direc2 = i2cw.DIRECTION_BACKWARD
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)
        i2cw.speed1 = int(float(spd/1.25))
        i2cw.speed2 = int(float(tspd/1.25))
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)

    def pspeed_psh(pspd):
        i2cw.speed1 = pspd
        i2cw.speed2 = pspd
        i2cw.drive(i2cw.speed2, i2cw.direc2, i2cw.speed1, i2cw.direc1)
        sleep(ptime)

    def full_stop():
        i2cw.stop_all()


class get_stat():
    def get_batt():
        return i2cw.get_status()[0]

    def measure_dist(counts):
        dist_edge_to_tofs = 30.0
        dist = []
        err = False
        for i in range(counts):
            distance = i2cw.get_status()[1]
            dist.append(distance)
        while 8190 in dist:
            dist.remove(8190)
            err = True
        if len(dist) == 0:
            retval = 8190
        else:
            retval = ((sum(dist)/len(dist))-dist_edge_to_tofs)
        return retval

    def get_distance(counts):
        dist = []
        for i in range(counts):
            distance = get_stat.measure_dist(5)
            dist.append(distance)
        return (median(dist))

    def precise_distance():
        mtime = 0.01
        dcm = 1
        dist0 = get_stat.measure_dist(20)
        sleep(mtime)
        dist1 = get_stat.measure_dist(20)
        sleep(mtime)
        dist2 = get_stat.measure_dist(20)
        sleep(mtime)
        dist3 = get_stat.measure_dist(20)
        sleep(mtime)
        dist4 = get_stat.measure_dist(20)
        sleep(mtime)
        dist5 = get_stat.measure_dist(20)
        sleep(mtime)
        dist6 = get_stat.measure_dist(20)
        sleep(mtime)
        dist7 = get_stat.measure_dist(20)
        sleep(mtime)
        dist8 = get_stat.measure_dist(20)
        acc_dist_array = [dist0, dist1, dist2, dist3, dist4, dist5, dist6, dist7, dist8]
        acc_dist_long = median(acc_dist_array)
        acc_dist = int(acc_dist_long*(10**dcm))/(10**dcm)
        return acc_dist

    def get_bumper():
        status = i2cw.get_status()
        swtch_sl = status[2]
        swtch_fl = status[3]
        swtch_fr = status[4]
        swtch_sr = status[5]
        return [swtch_sl, swtch_fl, swtch_fr, swtch_sr]
 

    def get_driving():
        stat = i2cw.get_mot_stat()
        return stat

class misc_func():
    def stopatcoll():
        i2cw.stop_at_collision()


    def latchet_bumper():
        return i2cw.read_latched_bumper()