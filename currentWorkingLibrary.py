#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Vehicles stored as drone1 and drone2. droneNumber is global identifier.
'''
from __future__ import print_function
from xbee import XBee
from dronekit import connect, VehicleMode, LocationGlobalRelative
import argparse
import os
import sys
import serial
import time
import json
import time


def switchDrones(droneNumber=1):
    #begin with drone #1
    #connect to proper Wi-Fi
    #disable network manager
    if droneNumber == 1:
        os.sys('nmcli -a c up "Auto SoloLink_3FA597"')
        time.sleep(7)
    else:
        os.sys('nmcli -a c up "Auto SoloLink_40D0C5"')        
        time.sleep(7)


def readRSSI(droneNumber=1):
    if(droneNumber == 1):
        fileToWrite = 'drone1'
        serial_port = serial.Serial('/dev/ttyUSB0', 9600)
    else:
        fileToWrite = 'drone2'
        serial_port = serial.Serial('/dev/ttyUSB1', 9600)
    xbee = XBee(serial_port)
    f= open("rssiReadings/"+ fileToWrite +".txt","a")
    for i in range(300):
        f.write(ord(xbee.wait_read_frame()['rssi']))
    f.close()

def averageRSSI(droneNumber=1):
    if (droneNumber ==1):
        with open('rssiReadings/drone1.txt','r') as f:
            data = [float(line.rstrip()) for line in f.readlines()]
            f.close()
        mean = float(sum(data))/len(data) if len(data) > 0 else float('nan')
    else:
        with open('rssiReadings/drone2.txt','r') as f:
            data = [float(line.rstrip()) for line in f.readlines()]
            f.close()
        mean = float(sum(data))/len(data) if len(data) > 0 else float('nan')
    return mean

def connectDrone(droneNumber=1):
    if droneNumber==1:
        drone1 = connect('udpin:0.0.0.0:14550', wait_ready=True)
#        arm_and_takeoff(1, drone1)
        print(" Global Location: %s" % drone1.location.global_frame)
        print(" Global Location (relative altitude): %s" % drone1.location.global_relative_frame)
        print(" Local Location: %s" % drone1.location.local_frame)
        print(" Attitude: %s" % drone1.attitude)
        return drone1
    else:
        drone2 = connect('udpin:0.0.0.0:14550', wait_ready=True) 
        arm_and_takeoff(1, drone2)
        return drone2

def arm_and_takeoff(aTargetAltitude, vehicle):
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def closeAll():
    global drone1
    drone1.mode = VehicleMode("RTL")
    time.sleep(2)
    drone1.close()
    time.sleep(30)
    global drone2
    drone2.mode = VehicleMode("RTL")
    time.sleep(2)
    drone2.close()

def currentLocation(droneNumber=1, vehicle=None):
        lat1 = vehicle.location.global_relative_frame.lat
        long1 = vehicle.location.global_relative_frame.lon
        altitude = vehicle.location.global_relative_frame.alt    
        return lat1, long1, altitude
def moveDrone(droneNumber=1, vehicle=None, latDelta=None, longDelta=None):
        vehicle.airspeed = 1
        lat1 = vehicle.location.global_relative_frame.lat
        long1 = vehicle.location.global_relative_frame.long
        altitude = vehicle.location.global_relative_frame.alt
        # point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
        vehicle.simple_goto(LocationGlobalRelative(lat1, long1, altitude))
   
# Close vehicle object before exiting script

