"""
Dylan Yinger
18-19 Drone Network Project
xbee_comm.py "test communication setup and read the usb data"
"""
import serial, time, datetime, sys
from xbee import XBee

import numpy as np

print ('Time Delay Switch to XBee')
time.sleep(10)
print ('Delay Over')
SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 9600
ser = serial.Serial(SERIALPORT, BAUDRATE)
xbee = XBee(ser)
while True:
    try:
        xbee.send("tx_long_addr", frame_id='\x00', dest_addr='\x00\x13\xA2\x00\x41\x7C\xA4\xC5',data='\x50\x49\x4E\x47')
        time.sleep(0.01)
        print('sending frame')
    except KeyboardInterrupt:
        break
ser.close()