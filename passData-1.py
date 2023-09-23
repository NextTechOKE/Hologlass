#this file gets the arduino port and then you send a command to the arduino :3
import serial 
arduinoData=serial.Serial('/dev/cu.BLTH', 115200)

while True:
    cmd=input('Please Enter Your Command: ')
    cmd=cmd+'\r'
    arduinoData.write(cmd.encode())