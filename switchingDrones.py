#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from dronekit import connect, VehicleMode
from pymavlink import mavutil
from datetime import datetime
import time
import sys
import os


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
#print("\nConnecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

vehicle.wait_ready('autopilot_version')

# Get all vehicle attributes (state)
print("\nGet all vehicle attribute values:")
"""
This is where we manipulate the properties and read in properly

"""
"""
Testing time it takes to send and recieve packet
"""

def cur_usec():
    """Return current time in usecs"""
    # t = time.time()
    dt = datetime.now()
    t = dt.minute * 60 + dt.second + dt.microsecond / (1e6)
    return t
intervalSum = 0.0
packageCount = 0
class MeasureTime(object):
    def __init__(self):
        self.prevtime = cur_usec()
        self.previnterval = 0
        self.numcount = 0
        self.reset()

    def reset(self):
        self.maxinterval = 0
        self.mininterval = 10000
        
    def log(self):
        #print "Interval", self.previnterval
        #print "MaxInterval", self.maxinterval
        #print "MinInterval", self.mininterval
        global intervalSum
        intervalSum += self.previnterval
        global packageCount
    #intervalSum/number of packets sent is the time per package sent.
        packageCount += 1
        sys.stdout.write('MaxInterval: %s\tMinInterval: %s\tInterval: %s\t, IntervalSum: %s\r' % (self.maxinterval,self.mininterval, self.previnterval, intervalSum/packageCount) )
        sys.stdout.flush()


    def update(self):
        now = cur_usec()
        self.numcount = self.numcount + 1
        self.previnterval = now - self.prevtime
        self.prevtime = now
        if self.numcount>1: #ignore first value where self.prevtime not reliable.
            self.maxinterval = max(self.previnterval, self.maxinterval)
            self.mininterval = min(self.mininterval, self.previnterval)
            self.log()


acktime = MeasureTime()

#Create COMMAND_ACK message listener.
@vehicle.on_message('COMMAND_ACK')
def listener(self, name, message):
    acktime.update()
    send_testpackets()

def send_testpackets():
    #Send message using `command_long_encode` (returns an ACK)
    msg = vehicle.message_factory.command_long_encode(
                                                    1, 1,    # target system, target component
                                                    #mavutil.mavlink.MAV_CMD_DO_SET_RELAY, #command
                                                    mavutil.mavlink.MAV_CMD_DO_SET_ROI, #command
                                                    0, #confirmation
                                                    0, 0, 0, 0, #params 1-4
                                                    0,
                                                    0,
                                                    0
                                                    )

    vehicle.send_mavlink(msg)
    print("sending test packet")

#Start logging by sending a test packet
send_testpackets()

#the packet isn't passed to here
print("Logging for 15 seconds")
for x in range(1,15):
    time.sleep(1)
    print("logging currently")
    #sum interval

"""
End Testing communication time
"""



# Get Vehicle Home location - will be `None` until first set by autopilot
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()
    if not vehicle.home_location:
        print(" Waiting for home location ...")
# We have a home location, so print it!        
print("\n Home location: %s" % vehicle.home_location)


# Set vehicle home_location, mode, and armed attributes (the only settable attributes)

print("\nSet new home location")
# Home location must be within 50km of EKF home location (or setting will fail silently)
# In this case, just set value to current location with an easily recognisable altitude (222)
my_location_alt = vehicle.location.global_frame
my_location_alt.alt = 0.0
vehicle.home_location = my_location_alt
print(" New Home Location (from attribute - altitude should be 0): %s" % vehicle.home_location)

#Confirm current value on vehicle by re-downloading commands
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()
print(" New Home Location (from vehicle - altitude should be 0): %s" % vehicle.home_location)


print("\nSet Vehicle.mode = GUIDED (currently: %s)" % vehicle.mode.name) 
vehicle.mode = VehicleMode("GUIDED")
while not vehicle.mode.name=='GUIDED':  #Wait until mode has changed
    time.sleep(1)


# Check that vehicle is armable
while not vehicle.is_armable:
    time.sleep(1)


#Define callback for `vehicle.attitude` observer
last_attitude_cache = None
def attitude_callback(self, attr_name, value):
    # `attr_name` - the observed attribute (used if callback is used for multiple attributes)
    # `self` - the associated vehicle object (used if a callback is different for multiple vehicles)
    # `value` is the updated attribute value.
    global last_attitude_cache
    # Only publish when value changes
    if value!=last_attitude_cache:
        print(" CALLBACK: Attitude changed to", value)
        last_attitude_cache=value

#print("\nAdd `attitude` attribute callback/observer on `vehicle`")     
vehicle.add_attribute_listener('attitude', attitude_callback)
time.sleep(2)
# Remove observer added with `add_attribute_listener()` specifying the attribute and callback function
vehicle.remove_attribute_listener('attitude', attitude_callback)


@vehicle.on_attribute('mode')   
def decorated_mode_callback(self, attr_name, value):
    # `attr_name` is the observed attribute (used if callback is used for multiple attributes)
    # `attr_name` - the observed attribute (used if callback is used for multiple attributes)
    # `value` is the updated attribute value.
    print(" CALLBACK: Mode changed to", value)

print(" Set mode=STABILIZE (currently: %s) and wait for callback" % vehicle.mode.name) 
vehicle.mode = VehicleMode("STABILIZE")

print(" Wait 2s so callback invoked before moving to next example")
time.sleep(2)

print("\n Attempt to remove observer added with `on_attribute` decorator (should fail)") 
try:
    vehicle.remove_attribute_listener('mode', decorated_mode_callback)
except:
    print(" Exception: Cannot remove observer added using decorator")



 
# Demonstrate getting callback on any attribute change
def wildcard_callback(self, attr_name, value):
    print(" CALLBACK: (%s): %s" % (attr_name,value))

print("\nAdd attribute callback detecting ANY attribute change")     
vehicle.add_attribute_listener('*', wildcard_callback)

print(" Wait 1s so callback invoked before observer removed")
time.sleep(1)

print(" Remove Vehicle attribute observer")    
# Remove observer added with `add_attribute_listener()`
vehicle.remove_attribute_listener('*', wildcard_callback)
    


# Get/Set Vehicle Parameters
print("\nRead and write parameters")
print(" Read vehicle param 'THR_MIN': %s" % vehicle.parameters['THR_MIN'])

print(" Write vehicle param 'THR_MIN' : 10")
vehicle.parameters['THR_MIN']=10
print(" Read new value of param 'THR_MIN': %s" % vehicle.parameters['THR_MIN'])


print("\nPrint all parameters (iterate `vehicle.parameters`):")
for key, value in vehicle.parameters.iteritems():
    print(" Key:%s Value:%s" % (key,value))
    

print("\nCreate parameter observer using decorator")
# Parameter string is case-insensitive
# Value is cached (listeners are only updated on change)
# Observer added using decorator can't be removed.
 
@vehicle.parameters.on_attribute('THR_MIN')  
def decorated_thr_min_callback(self, attr_name, value):
    print(" PARAMETER CALLBACK: %s changed to: %s" % (attr_name, value))


print("Write vehicle param 'THR_MIN' : 20 (and wait for callback)")
vehicle.parameters['THR_MIN']=20
for x in range(1,5):
    #Callbacks may not be updated for a few seconds
    if vehicle.parameters['THR_MIN']==20:
        break
    time.sleep(1)


#Callback function for "any" parameter
print("\nCreate (removable) observer for any parameter using wildcard string")
def any_parameter_callback(self, attr_name, value):
    print(" ANY PARAMETER CALLBACK: %s changed to: %s" % (attr_name, value))

#Add observer for the vehicle's any/all parameters parameter (defined using wildcard string ``'*'``)
vehicle.parameters.add_attribute_listener('*', any_parameter_callback)     
print(" Change THR_MID and THR_MIN parameters (and wait for callback)")    
vehicle.parameters['THR_MID']=400  
vehicle.parameters['THR_MIN']=30


## Reset variables to sensible values.
print("\nReset vehicle attributes/parameters and exit")
vehicle.mode = VehicleMode("STABILIZE")
#vehicle.armed = False
vehicle.parameters['THR_MIN']=130
vehicle.parameters['THR_MID']=500


#Close vehicle object before exiting script
print("\nClose vehicle object")
vehicle.close()

# Shut down simulator if it was started.
if sitl is not None:
    sitl.stop()

print("Completed")