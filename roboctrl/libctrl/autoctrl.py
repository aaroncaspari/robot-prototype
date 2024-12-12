#!/usr/bin/python3
# Copyright (C) Aaron Caspari 2022
import libctrl.ctrl as ctrl
import time
import random


class choice:

    def choose_odds(odds):
        nr = random.randint(0, 1000)
        if nr > 1000/odds:
            return True
        else:
            return False

    def choose_reaction():
        choice = random.randint(0, 1)
        return choice

    def choose_duration():
        choice = random.randint(0, 420)
        duration = float(choice/42)
        return duration


class reactions:

    def irritated_react(runmode, measures, pspd): 
        if runmode == True:
            spd1 = random.randint(20, 40)
            spd2 = random.randint(30, 50)
        else:
            spd1 = 0
            spd2 = 0
        if (choice.choose_odds(5)) and (runmode == True):
            chilltime = choice.choose_duration()
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


    def avoidance_1(mode, measures, spd, pspd, s_dist):
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
                return 'autorun'
            else:
                if mode != 1:
                    print("avd1r2Distance 1, 2:", dist1, dist2, "reacting...")
                    ctrl.drive.turn_left(pspd, spd)
                    time.sleep(0.5)
                    ctrl.drive.full_stop()
                    dist3 = ctrl.get_stat.get_distance(measures)
                if (dist3 >= dist2) and (dist_diff >= dist2 - dist3):
                    print("avd1 going on")
                    return 'autorun'
                if mode == 1:
                    print("adv1 choice diabled")
                    return 'autorun'
                elif choice.choose_reaction() == 0:
                    print("avd1 chose reacting")
                    return 'reactoprx'
                else:
                    print("avd1 chose adavd")
                    return 'add_avoid'
        except Exception as e:
            print("failure", e)


    def avoidance_2(mode, measures, spd, pspd, s_dist):
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
                return 'autorun'
            else:
                if mode != 1:
                    print("avd2r2Distance 1, 2:", dist1, dist2, "reacting...")
                    ctrl.drive.turn_right(pspd, spd)
                    time.sleep(0.5)
                    ctrl.drive.full_stop()
                    dist3 = ctrl.get_stat.get_distance(measures)
                if (dist3 >= dist2) and (dist_diff >= dist2 - dist3):
                    print("avd2 going on")
                    return 'autorun'
                if mode == 1:
                    print("adv2 choice disabled")
                    return 'autorun'
                elif choice.choose_reaction() == 0:
                    print("avd2 chose reacting")
                    return 'reactoprx'
                else:
                    print("avd2 chose adavd")
                    return 'add_avoid'
        except Exception as e:
            print("failure", e)


    def add_avoid(runmode, measures, pspd):
        print("addavoid")
        reactions.irritated_react(runmode, measures, pspd)
        time.sleep(0.1)
        if choice.choose_reaction() == 1:
            print("adav chose reacting")
            return 'reactoprx'
        else:
            print ("adav chose rollin'")
            return 'autorun'



