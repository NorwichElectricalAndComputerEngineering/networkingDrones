from droneNetworkLib import *
drone1=connectDrone()
arm_and_takeoff(3, drone1)
moveDrone(drone1, 1,1 )
closeAll(drone1)