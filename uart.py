import serial
import time
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600,8,serial.PARITY_NONE,1)

    #communicate with laptop
#while True:
    #received_data = ser.read()              #read serial port            
    #sleep(0.03)
    #data_left = ser.inWaiting()             #check for remaining byte
    #received_data += ser.read(data_left)
    #print (received_data)                   #print received data 
    #ser.write(received_data.decode('utf-8'))
    

    
    #loop back
while True:    
    my='hello'
    ser.write(my.encode('utf-8'))
    received_data = ser.read()
    sleep(0.03)
    data_left = ser.inWaiting()
    received_data += ser.read(data_left)
    print (received_data.decode('utf-8'))
    