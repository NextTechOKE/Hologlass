#this file gets the arduino port and then you send a command to the arduino :3
# /dev/cu.usbserial-DN01DOAE
import serial
import sys





arduinoData=serial.Serial('/dev/cu.usbserial-14210', 115200)

def data_write(text):
    arduinoData.write(text)



while True:
    cmd=input('Please Enter Your Command: ')
    cmd=cmd+'\r'
    arduinoData.write(cmd.encode())