from subprocess import call
import libctrl.i2cwrapper as i2cwrapper
from time import sleep
while True:
    if i2cwrapper.get_bat_voltage() <= float(6.9):
        i2cwrapper.stop_all()
        sleep(0.5)
        if i2cwrapper.get_bat_voltage() <= float(7.2):
            call('/usr/bin/systemctl poweroff -i', shell=True)
        else:
            pass
    else:
        sleep(5)

