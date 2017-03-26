# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:23:44 2017

@author: pi
"""

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import hammertime

hammertime.SerialOpen()
hammertime.LedWhite()

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
resolution = (640, 480)
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
image2 = image 
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.imshow("Image2", image2)


cv2.waitKey(0)

time.sleep(10)



hammertime.LedOff()

hammertime.SerialClose() 