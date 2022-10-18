deviceName = "/dev/ttyUSB0" 
import serial
from time import sleep
s = serial.Serial(deviceName, 9600) 
# cmd = cmd = b'$PCAS10,0*1C\r\n'
# s.write(cmd)
cmd = b'$PCAS04,2*1B\r\n'
s.write(cmd)

while True:
    received_data = s.read(s.inWaiting()) 
    if not received_data == "":
        print(received_data.decode()) 
    sleep(1)