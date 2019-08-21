#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # you can change this to Board if you prefere
GPIO.setwarnings(False)

relay1 = 17 # enter your relay gpio number here
relay2 = 23 # enter your relay gpio number here
relay3 = 27 # enter your relay gpio number here
relay4 = 22 # enter your relay gpio number here

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)

# set relay off you may need to change this to high if you relay board works active on low, also change state to 1 if this is the case.
GPIO.output(relay1, GPIO.LOW)
GPIO.output(relay2, GPIO.LOW)
GPIO.output(relay3, GPIO.LOW)
GPIO.output(relay4, GPIO.LOW)

#DURING THE BOOTUP, THE PUMPS WILL RUN * SECONDS SO ALL THE PUMPS ARE FULL,
#SO, WHEN YOU PRESS THE BUTTON, YOU WILL GET THE PERFECT MIXTURE
time.sleep(3)
GPIO.output(relay1, GPIO.HIGH)
GPIO.output(relay2, GPIO.HIGH)
GPIO.output(relay3, GPIO.HIGH)
GPIO.output(relay4, GPIO.HIGH)

# HOW MUCH SLEEP IS NEEDED IN ORDER TO FILL ALL THE PUMPS?
time.sleep()

# AFTER THE SLEEP, SHUT OFF THE PUMPS!
GPIO.output(relay1, GPIO.LOW)
GPIO.output(relay2, GPIO.LOW)
GPIO.output(relay3, GPIO.LOW)
GPIO.output(relay4, GPIO.LOW)
