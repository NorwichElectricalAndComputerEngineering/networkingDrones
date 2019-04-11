'''
This script was used to read RSSI every 5 yards to map the RSSI readings to distance. The target
and GCS were placed in the line of movement of the drone. The drone started 20 yards away moves 15yds
forward towards teh gcs/target and relays the target->drone RSSI to be read and averaged. If the RSSI
is not read a timeout error is raised and the drone increments 5 yards forwards. 
'''

from droneNetworkLib import * #imports all functions from the library created
import os
import sys
import signal#used for timeout error only works in Linux

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    


drone1 = connectDrone()#connects to drone 1
arm_and_takeoff(5, drone1)#target altitude and vehicle
time.sleep(2)# sleep

'''
Notes from testing:
RSSI range is greatly reduced from testing on a level plane. 3m of elevation reduces the distance read to approx 15yd
'''
location1 = currentLocation(drone1)#reads the current location (i.e. home location/gcs location)
#if the RSSI data is not reliable send the drone back to the origin location so the XBEE is facing the operator to transmit
latdelt = (44.1410224-44.1410633)# 5 yards towards baseball field
longdelt = -(72.662931 -72.6629073)#keep it at center field
'''
This function moves the drone 5 yards 3 times and has a 5 second timeout built in every time it reads RSSI. 
If RSSI is not averaged in that time it sends a timeout error to the handler function at the top.
This function only takes the two params.  

'''
for i in range(3):
    moveDrone(drone1, latdelt, longdelt)
    # Set the signal handler and a 10-second alarm
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(10)

# This function may hang indefinitely
    readRSSI(1)

    signal.alarm(0)#set the alarm back to 0
    print(averageRSSI(1))
    time.sleep(2)



closeAll(drone1)