import serial
from xbee import XBee
import time
import json
serial_port = serial.Serial('/dev/ttyUSB4', 9600)
#Export in json format. json.dumps(xbee.wait_read_frame())
xbee = XBee(serial_port)

while True:
    try:
        #print(xbee.readline())
        print(xbee.wait_read_frame())
    except KeyboardInterrupt:
        break
'''
with open('data.json', 'r') as json_data:
    acct = json.load(json_data)
    print(ord(acct["rssi1"]))
    print(ord(acct["rssi2"]))
    print(ord(acct["rssi3"]))
    print(ord(acct["rssi4"]))
    print(ord(acct["rssi5"]))
    print(ord(acct["rssi6"]))
    print(ord(acct["rssi7"]))
    print(ord(acct["rssi8"]))
    print(ord(acct["rssi9"]))
    print(ord(acct["rssi10"]))
    print(ord(acct["rssi11"]))
    print(ord(acct["rssi12"]))
    print(ord(acct["rssi13"]))
    print(ord(acct["rssi14"]))
    print(ord(acct["rssi15"]))

'''
