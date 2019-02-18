from __future__ import print_function
from dronekit import connect, VehicleMode
from pymavlink import mavutil
from Tkinter import *
from datetime import datetime
from xbee import XBee
import sys
import os
import argparse

#import serial

import time

global root
#vehicleNumber = True
#def changeVehicle(vehicleNumber):
#    if vehicleNumber == True:

#os.system('iwconfig wlx9cefd5ff0e3f')

import time

#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Print out vehicle state information. Connects to SITL on local PC by default.')
parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None


#Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()


# Connect to the Vehicle. 
#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
print("\nConnecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

vehicle.wait_ready('autopilot_version')

#os.system('iwconfig wlx9cefd5ff0bcd --connect udpin:0.0.0.14550')
'''        else:
        os.system('iwconfig wlx9cefd5ff0e3f --connect udpin:0.0.0.14550')
        connectionString = 'udpin:0.0.0.14550'
        print("\nConnecting to vehicle on: %s" % connectionString)
        vehicle = connect(connectionString, wait_ready=True)
#serial_port = serial.Serial('/dev/ttyUSB0', 9600)
'''
def print_data(data):
    print(data)
#xbee = XBee(serial_port, callback=print_data)
#for x in range(0, 3):
#    try:
#        time.sleep(0.001)
#    except KeyboardInterrupt:
#        break

#xbee.halt()
#serial_port.close()
vehicleNumber = False

def setMode(mode):
    vehicle.mode = VehicleMode(mode)

def updateGUI(label, value):#Connecting to vehicle on: udpin:0.0.0.14550
    label['text'] = value

def addObserverAndInit(name, cb):
    vehicle.add_attribute_listener(name, cb)


#changeVehicle(vehicleNumber)

root = Tk()
root.wm_title("microGCS - the worlds crummiest GCS")
frame = Frame(root)
frame.pack()

locationLabel = Label(frame, text = "No location", width=60)
locationLabel.pack()
attitudeLabel = Label(frame, text = "No Att", width=60)
attitudeLabel.pack()
modeLabel = Label(frame, text = "mode")
modeLabel.pack()

addObserverAndInit('attitude', lambda vehicle, name, attitude: updateGUI(attitudeLabel, vehicle.attitude))
addObserverAndInit('location', lambda vehicle, name, location: updateGUI(locationLabel, str(location.global_frame)))
addObserverAndInit('mode', lambda vehicle,name,mode: updateGUI(modeLabel, mode))

Button(frame, text = "Auto", command = lambda : setMode("AUTO")).pack()
Button(frame, text = "RTL", command = lambda : setMode("RTL")).pack()

root.mainloop()

