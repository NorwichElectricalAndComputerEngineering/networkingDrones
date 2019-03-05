#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dronekit import connect, VehicleMode, LocationGlobalRelative
import sys, time
import os

# Connect to UDP endpoint (and wait for default attributes to accumulate)
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
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
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt) 
        #Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
            print("Reached target altitude")
            break
        time.sleep(1)

arm_and_takeoff(13)

print("Set default/target airspeed to 4")
vehicle.airspeed = 4


# sleep so we can see the change in map
time.sleep(1)

os.system('sudo wifi connect DRONE1') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE1')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)


arm_and_takeoff(8)
print("Set default/target airspeed to 4")
vehicle.airspeed = 4

# sleep so we can see the change in map
time.sleep(1)

os.system('sudo wifi connect DRONE2') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE2')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 2 is going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(44.141937, -72.660260, 13)
vehicle.simple_goto(point1)

# sleep so we can see the change in map
time.sleep(2)

os.system('sudo wifi connect DRONE1') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE1')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 1 is going towards first point for 30 seconds ...")
point2 = LocationGlobalRelative(44.141843, -72.660318, 8)
vehicle.simple_goto(point2)

# sleep so we can see the change in map
time.sleep(2)

os.system('sudo wifi connect DRONE2') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE2')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 2 is going towards second point for 30 seconds ...")
point3 = LocationGlobalRelative(44.141657, -72.659381, 13)
vehicle.simple_goto(point3)

# sleep so we can see the change in map
time.sleep(2)

os.system('sudo wifi connect DRONE1') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE1')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 1 is going towards second point for 30 seconds ...")
point4 = LocationGlobalRelative(44.141535, -72.659438, 8)
vehicle.simple_goto(point4)

# sleep so we can see the change in map
time.sleep(2)

os.system('sudo wifi connect DRONE2') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE2')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 2 is going towards third point for 30 seconds ...")
point5 = LocationGlobalRelative(44.141376, -72.659540, 13)
vehicle.simple_goto(point5)

# sleep so we can see the change in map
time.sleep(2)

os.system('sudo wifi connect DRONE1') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE1')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 1 is going towards third point for 30 seconds ...")
point6 = LocationGlobalRelative(44.141256, -72.659608, 8)
vehicle.simple_goto(point6)

# sleep so we can see the change in map
time.sleep(2)

os.system('sudo wifi connect DRONE2') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE2')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 2 is going towards fourth point for 30 seconds ...")
point7 = LocationGlobalRelative(44.141647, -72.660381, 13)
vehicle.simple_goto(point7)

# sleep so we can see the change in map
time.sleep(2)

os.system('sudo wifi connect DRONE1') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE1')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Drone 1 is going towards fourth point for 30 seconds ...")
point8 = LocationGlobalRelative(44.141524, -72.660451, 8)
vehicle.simple_goto(point8)

# sleep so we can see the change in map
time.sleep(15)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

#Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()

os.system('sudo wifi connect DRONE2') #Change Wifi connection to 
time.sleep(6)
os.system('sudo wifi connect DRONE2')

# Connect to UDP endpoint (and wait for default attributes to accumulate) ???
target = sys.argv[1] if len(sys.argv) >= 2 else 'udpin:0.0.0.0:14550'
print('Connecting to ' + target + '...')
vehicle = connect(target, wait_ready=True)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

#Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()