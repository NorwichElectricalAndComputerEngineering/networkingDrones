import serial
from xbee import XBee
import time
import json
serial_port = serial.Serial('/dev/ttyUSB0', 9600)
#Export in json format. json.dumps(xbee.wait_read_frame())
xbee = XBee(serial_port)
while True:
        try:
                print(xbee.wait_read_frame()['rf_data'])
                #print(xbee.wait_read_frame())
        
        except KeyboardInterrupt:
                break
serial_port.close()
'''

'''