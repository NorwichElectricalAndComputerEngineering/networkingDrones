from currentWorkingLibrary import *
import os
import sys
drone1 = connectDrone(1)
readRSSI(1)
distance = averageRSSI(1)
arm_and_takeoff(3, drone1)#target altitude and vehicle
'''
Record all deltas of RSSI for drone1
and drone2 and direction travelled
'''

'''
determine the change in RSSI to lat and long change
'''
location1 = currentLocation(1, drone1)

print('Location: ', location1)