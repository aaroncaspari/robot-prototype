#!/usr/bin/python3
# Copyright (C) Arne Caspari, Aaron Caspari 2022
import smbus

bus = smbus.SMBus(1)

DEVADDR = 0x17
DIRECTION_FORWARD = 0x0
DIRECTION_BACKWARD = 0x80


def drive(speed2, direc2, speed1, direc1):
    bus.write_i2c_block_data(DEVADDR, 0x10, [speed2 | direc2, speed1 | direc1])


def stop_all():
    bus.write_i2c_block_data(DEVADDR, 0x10, [0 | DIRECTION_FORWARD, 0 | DIRECTION_FORWARD])


def get_status():
    conversion_factor = 3.3 / (1 << 12)
    vbat_factor = 3.0  # conversion factor from voltage divider
    bat_hi, bat_lo, range_hi, range_lo, gpios = bus.read_i2c_block_data(DEVADDR, 0x0, 5)
    raw_val = bat_lo | (bat_hi << 8)
    bat_level = (raw_val * conversion_factor * vbat_factor)+1.0
    tof_range = range_lo | (range_hi << 8)
    swtch_sl = gpios & 1
    swtch_fl = (gpios >> 1) & 1
    swtch_fr = (gpios >> 2) & 1
    swtch_sr = (gpios >> 3) & 1
    return bat_level, tof_range, swtch_sl, swtch_fl, swtch_fr, swtch_sr


def stop_at_collision():
    bus.write_byte_data(DEVADDR, 0x14, 0b1)

def read_latched_bumper():
    bumper = bin(bus.read_byte_data(DEVADDR, 0x5))
    return bumper


def get_mot_stat():
    speed_a, speed_b = bus.read_i2c_byte_data(DEVADDR, 0x10, 2)
    return speed_a, speed_b
