# networkingDrones
This project is used to control 3dr drones with the DroneKit SDK to trilaterate the position of a target with onboard serial comms devices (XBEE). 
Hello and thank you for looking at networkingDrones!
This repo assumes that you have dronekit installed and working on your device. 
This library also uses signal which is a linux specific library however you can transfer this to another device should you change signal for another timeout error reading scheme.

droneNetworkLib.py => This is the working library created to shorten some the time it takes to get up to speed on controlling a drone and dealing with the XBEE scripts used to read data. To use this type from droneNetworkLib import *
This imports all of the functions created.

fixedLocationFlight.py => has an example use of droneNetworkLib.py. It moves the drone based off of fixed increments. It reads RSSI at each position however, should the RSSI not be able to be read move the transmitter to and GCS in range of the transmitter on the drone. This library was tested with the user operating the GCS and the target transmitter 15 yards to the left of the drone as it moves at the second point (12yds downfield) and all of the components communicated without error.  

collectRSSI5yard.py => This is the most recent test conducted with a timeout error built into the RSSI. The value of RSSI is averaged over 50 samples. This incremental distance is great for determining the RSSI exponential decay for the distance mapping. 

distanceTesting contains readings of RSSI at several distances and different headings to determine the dropoff in biderectional environment as well as decay due to distance.

day1DistanceTesting has the key values detemined by the measurements in day1DistanceTesting (readings at ground level 1.5ft off ground both target and gcs) such as std.dev averages and an error. 

RSSIReadings contains .txt files that the averageRSSI() function uses. 

xbee_comm.py has an example script for transmitting frames to a destination xbee. This script runs on the transmitter. The pi onboard the drone contains a different script which transmits the rssi data as the rf_data. 

