import serial
from xbee import XBee
import time
import json
serial_port = serial.Serial('/dev/ttyUSB2', 9600)
#Export in json format. json.dumps(xbee.wait_read_frame())
xbee = XBee(serial_port)

while True:
    try:
        #print(xbee.readline())
        print(ord(xbee.wait_read_frame()['rssi']))
        file_path = "2meter.txt"
        with open(file_path, 'a') as file:
            file.write(str(ord(xbee.wait_read_frame()['rssi'])))
            file.write("\n")
    except KeyboardInterrupt:
        break