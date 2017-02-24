# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:30:46 2017

@author: pi
"""

import serial
import time

SERIAL_TIMEOUT = 10 #open port using 10 sec timeout

LED_OFF     = 'rgbi'
LED_WHITE   = 'RGBi'
LED_RED     = 'Rgbi'
LED_GREEN   = 'rGbi'
LED_BLUE    = 'rgBi'
LED_IR      = 'rgbI'

ser = serial.Serial('/dev/ttyACM0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=SERIAL_TIMEOUT, xonxoff=0, rtscts=0 )  # open serial port

print(ser.name)         # check which port was really used
time.sleep(1);

ser.flushInput()

def MotorStart():
    ser.write('M')     # write a string
    time.sleep(0.01)
    t1 = time.time()
    resp = ser.read(1)
    t2 = time.time()
    print('Response:'+resp + ' Latency:' + t2-t1)

def MotorStop():
    ser.write('m')     # write a string
    time.sleep(0.01) 
    resp = ser.read(1)
    print('Response: '+resp)

def MotorAdvanceOneFrame():
    ser.flushInput()
    t1 = time.time()
    ser.write('A')     # write a string
    resp = ser.read(3)  # shoud acc with A and then M for motor start and m for motor stop
    t2 = time.time()
    print('Response:'+resp + ' Latency:' + '%.2f' % (t2-t1))

def LedCmd(cmd):
    ser.flushInput()
    t1 = time.time()
    ser.write(cmd)     # write a string
    resp = ser.read(len(cmd))  # shoud acc with RGBi
    t2 = time.time()
    print('Response:'+resp + ' Latency:' + '%.2f' % (t2-t1))




MotorAdvanceOneFrame()
LedCmd(LED_WHITE)
time.sleep(1);
LedCmd(LED_RED)
time.sleep(1);
LedCmd(LED_GREEN)
time.sleep(1);
LedCmd(LED_BLUE)
time.sleep(1);
LedCmd(LED_IR)
time.sleep(1);
LedCmd(LED_OFF)
time.sleep(1);



time.sleep(.10);
print('closing port')
ser.close()             # close port
