#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#from git import Repo
from subprocess import call

button1 = 26    #6
GPIO.setup(button1, GPIO.IN)

while True:
# check if switch is pressed and keep checking
        while GPIO.input(button1) == 1:
                print "waiting for switch press"
                sleep(0.5)

        else:
                # checks current relay state and changes it to the other.
                if GPIO.input(button1) == 0 :
                        print("shutting Down?? HOLD 3 sec")
                        sleep(3.0)
                        #call("sudo shutdown -h now", shell=True)
                        if GPIO.input(button1) == 0:
                                print("shutting Down 4 Real!   BYE")
                                call("sudo shutdown -h now", shell=True)
                        else:
                                print("Just Kidding")
