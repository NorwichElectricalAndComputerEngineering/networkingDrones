from currentWorkingLibrary import *
import os
import sys
drone1 = connectDrone(1)
arm_and_takeoff(3, drone1)#target altitude and vehicle
time.sleep(2)

readRSSI(1)
RSSI1 = averageRSSI(1)

'''
Notes from testing:

'''
location1 = currentLocation(1, drone1)
latdelt = (44.1407269-44.1411495)/4# 50yards/4 
longdelt = -(72.6629716-72.6625669)/3
moveDrone(1, drone1, latdelt, longdelt)
location2 = currentLocation(1, drone1)

readRSSI(1)
RSSI2 = averageRSSI(1)

moveDrone(1, drone1, latdelt, 0)
location3 = currentLocation(1, drone1)

readRSSI(1)
RSSI3 = averageRSSI(1)

moveDrone(1, drone1, latdelt, 0)
location4 = currentLocation(1, drone1)

readRSSI(1)
RSSI4 = averageRSSI(1)

print('Location1: ', location1)
print('Location2: ', location2)
print('Location3: ', location3)
print('Location4: ', location4)

print('RSSI 1: ', RSSI1)
print('RSSI 1: ', RSSI2)
print('RSSI 1: ', RSSI3)
print('RSSI 1: ', RSSI4)

'''
drone1.attitude => Attitude:pitch=-0.0473402887583,yaw=0.9554438591,roll=-0.00338281784207
drone1.attitude.yaw = something 
'''
closeAll(drone1)