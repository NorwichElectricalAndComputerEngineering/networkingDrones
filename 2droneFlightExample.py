'''
This script was used to move 2 drones, read RSSI every 5 yards. The two drones should be placed 
at least 10 yards apart to ensure that they do not collide midair. Both drones move forward in 5yard
increments towards the baseball field from the practice football field. 
'''

from droneNetworkLib import * #imports all functions from the library created
import os
import sys
import signal#used for timeout error only works in Linux

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    


drone1 = connectDrone()#connects to drone 1
arm_and_takeoff(5, drone1)#target altitude and vehicle
locationOfDrone1 = currentLocation(drone1)#reads the current location (i.e. home location/gcs location)

switchDrones(2)
drone2 = connectDrone()
arm_and_takeoff(5, drone2)
locationOfDrone2 = currentLocation(2, drone2)

latdelt = (44.1410224-44.1410633)# 5 yards towards baseball field
longdelt = -(72.662931 -72.6629073)#keep it at center field

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