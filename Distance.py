import time
import RPi.GPIO as GPIO
import os
import sys

import copy
import uuid
import logging

from datetime import datetime, timezone








    



GPIO.setmode(GPIO.BCM)
echo = 21
trigger = 23
led1 = 13
led2 = 12
GPIO.setup(echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(trigger, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led2, GPIO.OUT, initial=GPIO.HIGH)

while True:
    
    GPIO.output(trigger, False)
    print (".")
    time.sleep(.1)
    
    GPIO.output(trigger, True)                  #Set TRIG as HIGH
    time.sleep(0.00002)                     #Delay of 0.00001 seconds
    GPIO.output(trigger, False)                 #Set TRIG as LOW

    while GPIO.input(echo)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(echo)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance_cm = round(distance, 1)
    distance_in = round(distance/2.54, 1)
    distance_ft = round((distance/2.54)/12, 1)
    
       
    
            
    
    #Round to two decimal points

    if distance_cm > 2 and distance_cm < 400:      #Check whether the distance is within range
        print ("Distance: ",distance_cm - 0.5, " cm   ", distance_in, " in    ", distance_ft, " ft")  #Print distance with 0.5 cm calibration
        readings = {'distance': distance_in}
        
        if distance_cm > 2 and distance_in < 70:
            GPIO.output(led2,0)
            time.sleep(1)
            GPIO.output(led2, 1)
               
    else:
        print ("Out of Range")                   #display out of range
