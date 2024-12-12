#!/usr/bin/python3
# Copyright (C) Aaron Caspari 2022
import libctrl.ctrl as ctrl
import sys
import time
import random

measures = 20
if sys.argv[1] == '--dryrun':
    runmode = False
    spd = 0
    pspd = 0
    tspd = 0
else:
    runmode = True
    spd = int(sys.argv[1])
    pspd = int(float(spd/2))
    p_tspd = int(spd/1.07)
    recurse = 0
    if p_tspd <= 15:
        tspd = 15
    else:
        tspd = p_tspd
    if sys.argv[1] == 0:
        spd = 0
        pspd = 0
        tspd = 0
    if sys.argv[1] == 1:
        spd = 25
        pspd = 25
        tspd = 25
s_dist = int(sys.argv[2])


def choose_reaction():
    choice = random.randint(0, 1)
    return choice


def irritated_react():
    if runmode == True:
        spd1 = random.randint(20, 40)
        spd2 = random.randint(30, 50)
    else:
        spd1 = 0
        spd2 = 0
    if (random.randint(0, 420) <= 100) and (runmode == True):
        chilltime = float(random.randint(0, 420)/42)
        print("chillin'", chilltime, "seconds...")
        time.sleep(chilltime)
    tspd1 = int(spd1/1.3)
    tspd2 = int(spd2/1.3)
    dist1 = ctrl.get_stat.get_distance(measures)
    print("irritated:", spd1, spd2, dist1)
    time.sleep(0.01)
    ctrl.drive.turn_left(pspd, tspd2)
    time.sleep(0.5)
    ctrl.drive.turn_right(pspd, tspd1)
    time.sleep(0.3)
    ctrl.drive.drive_backward(spd1, pspd)
    time.sleep(0.1)
    dist2 = ctrl.get_stat.get_distance(measures)
    return dist1, dist2


def avoidance_1(mode):
    try:
        print("reacting...")
        ctrl.drive.drive_backward(spd, pspd)
        time.sleep(0.2)
        ctrl.drive.full_stop()
        dist1 = ctrl.get_stat.get_distance(measures)
        ctrl.drive.turn_right(pspd, spd)
        time.sleep(0.2)
        ctrl.drive.full_stop()
        dist2 = ctrl.get_stat.get_distance(measures)
        dist_diff = (dist1 - dist2)
        if (dist1 <= (dist2+(dist1/dist2))) and (dist2 >= s_dist):
            print("avd1r1Distance 1, 2:", dist1, dist2, "keeping ago")
            autorun()
        else:
            print("avd1r2Distance 1, 2:", dist1, dist2, "reacting...")
            ctrl.drive.turn_left(pspd, spd)
            time.sleep(0.5)
            ctrl.drive.full_stop()
            dist3 = ctrl.get_stat.get_distance(measures)
            if (dist3 >= dist2) and (dist_diff >= dist2 - dist3):
                print("avd1 going on")
                autorun()
            if mode == 1:
                print("adv1 choice diabled")
                autorun()
            elif choose_reaction() == 0:
                print("avd1 chose reacting")
                reactoprx()
            else:
                print("avd1 chose adavd")
                add_avoid()
    except Exception as e:
        print("failure", e)


def avoidance_2(mode):
    try:
        print("reacting...")
        ctrl.drive.drive_backward(spd, pspd)
        time.sleep(0.2)
        ctrl.drive.full_stop()
        dist1 = ctrl.get_stat.get_distance(measures)
        ctrl.drive.turn_left(pspd, spd)
        time.sleep(0.2)
        ctrl.drive.full_stop()
        dist2 = ctrl.get_stat.get_distance(measures)
        dist_diff = (dist1 - dist2)
        if (dist1 <= (dist2+(dist1/dist2))) and (dist2 >= s_dist):
            print("avd2r1Distance 1, 2:", dist1, dist2, "keeping ago")
            autorun()
        else:
            print("avd2r2Distance 1, 2:", dist1, dist2, "reacting...")
            ctrl.drive.turn_right(pspd, spd)
            time.sleep(0.5)
            ctrl.drive.full_stop()
            dist3 = ctrl.get_stat.get_distance(measures)
            if (dist3 >= dist2) and (dist_diff >= dist2 - dist3):
                print("avd2 going on")
                autorun()
            if mode == 1:
                print("adv2 choice disabled")
                autorun()
            elif choose_reaction() == 0:
                print("avd2 chose reacting")
                reactoprx()
            else:
                print("avd2 chose adavd")
            add_avoid()
    except Exception as e:
        print("failure", e)


def reactoprx():  # react to approaching objects
    try:
        choice = choose_reaction()
        if choice == 0:
            print("reacprx chose avd1")
            avoidance_1(0)
        elif choice == 1:
            print("reacprx chose avd2")
            avoidance_2(0)
    except Exception as e:
        print("failure", e)


def autorun():
    driving = False
    print("runmode:", runmode)
    try:
        while ctrl.get_stat.get_distance(measures) >= s_dist:
            tbump = ctrl.get_stat.get_bumper()
            if runmode == True:
                uspd = random.randint(int(tspd), int(spd*1.75))
                if driving == False:
                    ctrl.misc_func.stopatcoll()
                    ctrl.drive.drive_forward(int(uspd), int(uspd/2))
                    driving = True
            if any(tbump):
                bumper = ctrl.misc_func.latchet_bumper()
                bump = bumper
                print("bumped!", bump, tbump)
                if (bump == 0b1) or (bump == 0b10) or (bump == 0b11):
                    print("avd1")
                    avoidance_1(1)
                if (bump == 0b100) or (bump == 0b1000) or (bump == 0b1100):
                    print("avd2")
                    avoidance_2(1)
                else:
                    print("illegal byte")
                break
        print("danger detected:", ctrl.get_stat.measure_dist(1), "mm")
        reactoprx()
    except Exception as e:
        print("Failure", e)


def add_avoid():
    print("addavoid")
    irritated_react()
    time.sleep(0.1)
    if choose_reaction() == 1:
        print("adav chose reacting")
        reactoprx()
    else:
        print ("adav chose rollin'")
        autorun()

print("\nRollin' on...\n")
autorun()
