# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:50:56 2017

opencv stuff taken from this guide:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

@author: pi
"""

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import hammertime
import png
 
res = (640,480) 
redGain = 1.0
DELTAGAIN = 0.025
DELTASHUTTERSPEED = 1000 
blueGain = 1.0
shutterspeed_us = 20000
iso = 100


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = res
camera.framerate = 16
# allow the camera to warmup
time.sleep(1)
camera.awb_mode = 'off'
camera.awb_gains = (redGain, blueGain)
camera.shutter_speed = shutterspeed_us
camera.exposure_mode = 'off'

camera.vflip = True
camera.iso = 100
camera.DRC_STRENGTHS


rawCapture = PiRGBArray(camera, size=res)
 

h = np.zeros((300,256,3))
h4 = np.zeros((300,256,3))


bins = np.arange(256).reshape(256,1)
bins4 = np.arange(64).reshape(64,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]


hammertime.SerialOpen()

def showCameraSettings():
    print "Iso: {1}",camera.iso
    print "Shutter: ", camera.shutter_speed
    print "Gain [red,blue]: ", camera.awb_gains
    print "Exposure compensation: ",camera.exposure_compensation
    
def updateCameraSettings():
    camera.shutter_speed = shutterspeed_us
    camera.awb_gains = (redGain, blueGain)
    camera.iso = iso
        
def displayHistogram(input):
    h = np.zeros((300,256,3))
    h4 = np.zeros((900,256,3))
    for ch, col in enumerate(color):
        hist_item = cv2.calcHist([input],[ch],None,[256],[0,255])
        cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
        hist=np.int32(np.around(hist_item))
        pts = np.column_stack((bins,hist))
        pts4 = np.column_stack((bins4,hist.reshape(4,64).sum(0)))
#        cv2.polylines(h,[pts],True,col,lineType=4)

        corner1 = np.array([[0,0]])
        corner2 = np.array([[255,0]])
        pts2=np.append(pts, corner1,axis=0)

        cv2.fillPoly(h,[pts2],col,lineType=8)
        print pts.shape
        #cv2.polylines(h4,[pts4],False,col)

    h=cv2.flip(h,0)
    #h4=cv2.flip(h4,0)
    
    cv2.imshow('colorhist',h)
    #cv2.imshow('colorhist-4',h4)  


 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
    

    
    x = int(0.21*res[0] //1)
    y = int(0.24*res[1] //1)
    w = int(0.48*res[0] //1)
    h = int(0.52*res[1] //1)
    
    #image = image[y:h,x:w]

#    hist = cv2.calcHist([image],[0],None,[256],[0,256])   
    	# show the frame
    image2 = image[ y:y+h, x:x+w].copy()
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), thickness=1, lineType=8, shift=0)
    cv2.imshow("Frame", image)

    
    cv2.imshow("Frame2", image2)

    
    displayHistogram(image2)
  

    
    key = cv2.waitKey(1) & 0xFF
     
    	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
     
    	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        print "exit"
        hammertime.SerialClose()

      #plt.hist(image.ravel(),256,[0,256]);plt.show()
        break

    if key == ord("+"):
        shutterspeed_us += DELTASHUTTERSPEED
        updateCameraSettings()

    if key == ord("-"):
        shutterspeed_us -= DELTASHUTTERSPEED
        updateCameraSettings()

    if key == ord("1"):
        redGain = redGain-DELTAGAIN
        updateCameraSettings()

    if key == ord("2"):
        redGain = redGain+DELTAGAIN
        updateCameraSettings()

    if key == ord("4"):
        blueGain = blueGain-DELTAGAIN
        updateCameraSettings()

    if key == ord("5"):
        blueGain = blueGain+DELTAGAIN
        updateCameraSettings()


    if key == ord("W"):
       hammertime.LedWhite()

    if key == ord("A"):
       hammertime.MotorAdvanceOneFrame()


    if key == ord("w"):
       hammertime.LedOff()


    if key == ord("R"):
       hammertime.LedRed()
    if key == ord("G"):
       hammertime.LedGreen()
    if key == ord("B"):
       hammertime.LedBlue()

    if key == ord("I"):
       hammertime.LedIr()

    if key == ord("s"):
       i=image2
       f=open('test16b.png','wb')
       w = png.Writer(len(i),len(i[0]),bitdepth=16)
       w.write()
       test16b = image2.astype('uint16')
       cv2.imwrite('test16b.png',image2 )
       print "type: ", test16b.dtype
       
    
    if key == ord("M"):
       hammertime.MotorStart()

    if key == ord("m"):
       hammertime.MotorStart()
        
    if key == ord("d"):
       showCameraSettings()
        
      
