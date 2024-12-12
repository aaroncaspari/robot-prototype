import libctrl.i2cwrapper as i2cw
import libctrl.ctrl as ctrl
import sys
import argparse
direction1 = ''
direction2 = ''

parser = argparse.ArgumentParser(description="Control the robot through a commandline")

parser.add_argument("-s", "--speed", dest="spd", action="store", type=int, default=0, help='set speed')

parser.add_argument('-d', '--distance', dest='dist', action='store_true', help='get tof-sensor distance')

parser.add_argument("-b", '--battery', dest='batt', action='store_true', help='get battery voltage')

parser.add_argument("-o", "--optional", dest="optional", action="store_true")

parser.add_argument("values", metavar="VALS", type=float, nargs="*", help="some values")

args = parser.parse_args()

if args.batt == True:
    print("\nBattery voltage: ", ctrl.get_stat.get_batt(), "V")
if args.dist == True:
    print("\nDistance: ", ctrl.get_stat.get_distance(), "mm")
if args.spd == (0 or False):
    print("stoped.")
    ctrl.drive.full_stop()
else:
    try:
        speed1 = int(args.spd)
        direction1 = sys.argv[2]
        speed2 = int(args.spd)
        direction2 = sys.argv[4]
    except:
        speed1 = 0
        speed2 = 0
        direction1 = 'fwd'
        direction2 = 'fwd'

if direction1 == 'fwd':
    direc1 = i2cw.DIRECTION_FORWARD
elif direction1 == 'bwd':
    direc1 = i2cw.DIRECTION_BACKWARD
else:
    direc1 = i2cw.DIRECTION_FORWARD
    speed1 = 0
if direction2 == 'fwd':
    direc2 = i2cw.DIRECTION_FORWARD
elif direction2 == 'bwd':
    direc2 = i2cw.DIRECTION_BACKWARD
else:
    direc2 = i2cw.DIRECTION_FORWARD
    speed2 = 0


i2cw.drive(speed2, direc2, speed1, direc1)