import serial
from xbee import XBee
import time
import json
serial_port = serial.Serial('/dev/ttyUSB3', 9600)
#Export in json format. json.dumps(xbee.wait_read_frame())
xbee = XBee(serial_port)
for i in range(500):
    #print(xbee.readline())
    print(ord(xbee.wait_read_frame()['rssi']))
    file_path = "30yard.txt"
    with open(file_path, 'a') as file:
        file.write(str(ord(xbee.wait_read_frame()['rssi'])))
        file.write("\n")
