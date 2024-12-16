#!/usr/bin/python3
# Copyright (C) Aaron Caspari 2022
from sshkeyboard import listen_keyboard, stop_listening  # (to self) why?
import sys
import libctrl.ctrl as ctrl
import libctrl.ctrl as stpc
from time import sleep
import traceback
wannaquit = int(1)
spd = int(0)
# get speed variables.
try:
    spd = int(sys.argv[1])  # PLEASE dont set spd to 100 (overcurrent)
    if spd == 0:
        pass
    elif spd <= 7:
        spd = int(7)
except:
    if len(sys.argv) == 1:
        spd = 30
    elif sys.argv[1] == '-h' or '--help':
        print('|> argument 1 has to be an <integer> for power %.(1-100)\n|<wasd> + <qe> + <yx> control.\n|<p> for stop.\n|<n> for tof sensor.\n|<m> for battery voltage.\n|<space> for quit.')
        sleep(1)
        print("\n||wait for >ready<||")
        sleep(0.75)
        sys.exit(0)
'''
spd = speed
tspd = turnspeed
pspd = prespeed for getting moving/not overpoweringstpc
'''
try:
    tspd = int(float(spd)/2)
    if spd < 14:
        tspd = int(8)
    if spd > 89:
        tspd = int(65)
except Exception as e:
    print("failed to set turn-speed", e)
    pass
try:
    pspd = int(float(spd)*1.75)
    if pspd >= 41:
        pspd = int(40)
    elif pspd <= 19:
        pspd = int(20)
except Exception as e:
    print(e)

if spd == 0:
    spd = 0
    pspd = 0
    tspd = 0

ptime = float(0.00420)


def quiting(quit_try):
    if quit_try == 10:
        print("Forcing...")
        ctrl.Drive.full_stop()
        sleep(1)
        sys.exit(2)
    bye = str(input("really quit? [y/N]: "))
    try:
        if bye == '':
            if (quit_try >= 6) and (quit_try != 9):
                print("forcing in: ", (-quit_try+9))
            runrmt(quit_try+1)
        if bye in ['n', 'N']:
            quit_try = 0
            runrmt(quit_try)
        if bye in ['y', 'Y']:
            print("\nbye.")
            ctrl.Drive.full_stop()
            sys.exit(0)
        elif bye not in ['y', 'Y', 'n', 'N']:
            if quit_try != 9:
                print("forcing in:", (-quit_try+9))
            quiting(quit_try+1)
    except Exception as e:
        print("failure", e)
        runrmt(quit_try+1)


def runrmt(wannaquit):
    def press(key):
        global spd
        if key == "w":  # directions
            try:
                print("w pressed")
                ctrl.Drive.drive_forward(spd, pspd)
                stpc.stopatcoll()
                print("driving forward...")
            except Exception as e:
                print("failed", e)
                pass
        elif key == "s":
            try:
                print("s pressed")
                ctrl.Drive.drive_backward(spd, pspd)
                stpc.stopatcoll()
                print('driving backward...')
            except Exception as e:
                print("failed", e)
                pass
        elif key == "a":
            try:
                print("a pressed")
                ctrl.Drive.turn_left(pspd, tspd)
                print('turning left...')
            except Exception as e:
                print("failed", e)
                pass
        elif key == "d":
            try:
                print("d pressed")
                ctrl.Drive.turn_right(pspd, tspd)
                print('turning right...')
            except Exception as e:
                print("failed", e)
                pass
        elif key == 'p':  # stop all
            try:
                print("p pressed")
                # ctrl.prspeed_fw(pspd)
                # sleep(0.1)
                ctrl.Drive.full_stop()
                print('stoped.')
            except Exception as e:
                print("failed", e)
                pass
        elif key == 'e':  # for curves
            try:
                print("e pressed")
                ctrl.Drive.drive_fwright(spd, pspd, tspd)
                stpc.stopatcoll()
                print('driving right...')
            except Exception as e:
                print("failed", e)
                pass
        elif key == 'x':
            try:
                print("x pressed")
                ctrl.Drive.drive_bwright(spd, pspd, tspd)
                stpc.stopatcoll()
                print('backing right...')
            except Exception as e:
                print("failed", e)
                pass
        elif key == 'q':
            try:
                print("q pressed")
                ctrl.Drive.drive_fwleft(spd, pspd, tspd)
                stpc.stopatcoll()
                print('driving left...')
            except Exception as e:
                print("failed", e)
                pass
        elif key == 'y':
            try:
                print("y pressed")
                ctrl.Drive.drive_bwleft(spd, pspd, tspd)
                stpc.stopatcoll()
                print('backing left...')
            except Exception as e:
                print("failed", e)
                pass
        elif key == 'space':  # quit
            try:
                stop_listening()
            except Exception as e:
                print("problem leaving...", e)
        elif key == '1':  # for setting speed
            try:
                spd = int(10)
                print("speed set to 10%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '2':
            try:
                spd = int(20)
                print("speed set to 20%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '3':
            try:
                spd = int(30)
                print("speed set to 30%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '4':
            try:
                spd = int(40)
                print("speed set to 40%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '5':
            try:
                spd = int(50)
                print("speed set to 50%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '6':
            try:
                spd = int(60)
                print("speed set to 60%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '7':
            try:
                spd = int(70)
                print("speed set to 70%")
            except Exception as e:
                print("failed to set speed", e)
        elif key == '8':
            try:
                spd = int(80)
                print("speed set to 80%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '9':
            try:
                spd = int(90)
                print("speed set to 90%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == 'b':
            try:
                spd = int(100)
                print("speed set to 100%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == '0':
            try:
                spd = int(0)
                print("speed set to 0%")
            except Exception as e:
                print("failed to set speed", e)
                pass
        elif key == 'm':
            try:  # get battery voltage level; corrected
                dcm = 2
                volt = ctrl.get_batt()
                pvolt = int(volt*(10**dcm))/(10**dcm)
                print("Voltage: ", pvolt, "V")
            except Exception as e:
                print("failed get battery voltage", e)
                pass
        elif key == 'n':
            try:
                #  get the distance / free space directly in front of the robot; corrected for case measures
                pdist = int(ctrl.get_distance(10))
                if pdist == [8190 or 8161]:
                    pdist = '>failure<'
                print("Distance: ", pdist, "mm")
            except Exception as e:
                print("failed to get tof data", e)
                traceback.print_exc()
                pass
        elif key == 'f':
            try:
                dcm = 1
                #  get more accurate distance by averaging multiple pings
                dist1 = float(ctrl.precise_distance())
                print("---\nDistance: ", dist1, "mm")
                dist2 = float(ctrl.precise_distance())
                print("Distance: ", dist2, "mm")
                dist3 = float(ctrl.precise_distance())
                print("Distance: ", dist3, "mm")
                avg = (dist1+dist2+dist3)/3
                pavg = int(avg*(10**dcm))/(10**dcm)
                print("avg.:", pavg, "mm\n---")
            except Exception as e:
                print("failed to get tof data", e)
                traceback.print_exc()
                pass

    print("ready")
    listen_keyboard(on_press=press)
    ctrl.Drive.full_stop()
    quiting(wannaquit)


runrmt(wannaquit)
