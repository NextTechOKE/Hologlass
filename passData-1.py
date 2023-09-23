#this file gets the arduino port and then you send a command to the arduino :3
# /dev/cu.usbserial-DN01DOAE
import serial 
arduinoData=serial.Serial('/dev/cu.usbserial-14210', 115200)

while True:
    cmd=input('Please Enter Your Command: ')
    cmd=cmd+'\r'
    arduinoData.write(cmd.encode())