

#This code will show you an image that you have either loaded as an input argumet i.e. python3 imgRead("img.jpg")
#or this code will take an image using your PiCamera
#I created this code utilizing code I found on the pyimagesearch website.  Go google it and check it out.

import numpy as np
import cv2
import sys
from picamera.array import PiRGBArray #https://picamera.readthedocs.io/en/release-1.13/
#This sintax (from ... import...) only imports a single class/fuction from the module.  PiRGB in this case.
from picamera import PiCamera
import time

try:
        #This line looks in the sys module which lets you access command line arguments.  sysy.argv[1] is the input argument to the function
        #if there is an input argument, the try statement is exicuted

        fn = sys.argv[1]
        img = cv2.imread(fn)
except:
        #If there is an error in the try statement, if there is no input argument for example, the except statement runs and initializes the camera
        
        #This sets camera as our picamera object
        camera = PiCamera()
        #OpenCv uses RGB arrays in it's functions, so we utilize the PiRGBArray function to capture in the format we desire.
        #The documentation goes into more detail https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera
        rawCapture = PiRGBArray(camera)
         
        # allow the camera to warmup
        time.sleep(0.1)
         
        # grab an image from the camera 
        camera.capture(rawCapture, format="bgr")
        img = rawCapture.array


# Load an color image 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',600,600)

#make sure the image is facing the right direction
img=cv2.flip(img,0)

#show the image
cv2.imshow('image',img)

#waitKey is a function that waits for you to touch a key.  It is required in OpenCV to show images often times.  
#The 0 in waitkey denotes the function should waith indefinatly for a key stroke.  If you put a number, it will wait for that many milliseconds
keyStroke=cv2.waitKey(0)

#If keyStoke in 27 (the ansi key numeral for the esp key) quit from the window
if keyStroke == 27:
    cv2.destroyAllWindows()
