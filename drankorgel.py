#!/usr/bin/python


import RPi.GPIO as GPIO
import time
switch1 = 24 # enter your switch gpio number here
switch2 = 20 # enter your switch gpio number here

relay1 = 17 # enter your relay gpio number here
relay2 = 23 # enter your relay gpio number here
relay3 = 27 # enter your relay gpio number here
relay4 = 22 # enter your relay gpio number here

state1 = 0
state2 = 0


GPIO.setmode(GPIO.BCM) # you can change this to Board if you prefere
GPIO.setwarnings(False)
GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)
# set relay off you may need to change this to high if you relay board works active on low, also change state to 1 if this is the case.
GPIO.output(relay1, GPIO.LOW)
GPIO.output(relay2, GPIO.LOW)
GPIO.output(relay3, GPIO.LOW)
GPIO.output(relay4, GPIO.LOW)
while True:

# check if switch is pressed and keep checking
        while GPIO.input(switch1) == 1 and GPIO.input(switch2) == 1:
                print "waiting for switch press"
                #print(GPIO.input(switch1))
                #print(GPIO.input(switch2))
                time.sleep(0.5)

        else:
                # checks current relay state and changes it to the other.
                if GPIO.input(switch2) == 0 and GPIO.input(switch1) == 1:
                        print "Setting SWITCH 1  gpio high"
                        #print(GPIO.input(switch1))
                        #print(GPIO.input(switch2))
                        state1 = 1
                        GPIO.output(relay3, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(relay3, GPIO.LOW)
                        GPIO.output(relay4, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(relay4, GPIO.LOW)
                        state1 = 0
                        #print(state1)
                        #print(state2)
                        time.sleep(1)

                elif GPIO.input(switch1) == 0 and GPIO.input(switch2) == 1:
                #elif state2 == 0:
                        print "Setting SWITCH 2  gpio high"
                        #print(GPIO.input(switch1))
                        #print(GPIO.input(switch2))
                        state2 = 1
                        GPIO.output(relay1, GPIO.HIGH)
                        time.sleep(3)
                        GPIO.output(relay1, GPIO.LOW)
                        GPIO.output(relay2, GPIO.HIGH)
                        time.sleep(3)
                        GPIO.output(relay2, GPIO.LOW)
                        state2 = 0
                        #print(state1)
                        #print(state2)
                        time.sleep(1)
                else:
                        print "setting gpio low"
                        state1 = 0
                        state2 = 0
                        GPIO.output(relay1, GPIO.LOW)
                        GPIO.output(relay2, GPIO.LOW)
                        GPIO.output(relay3, GPIO.LOW)
                        GPIO.output(relay4, GPIO.LOW)
                        time.sleep(1)
# check for switch released and keep checking
        while GPIO.input(switch1) == 0 or GPIO.input(switch2) == 0:
                print "waiting for switch release"
                time.sleep(0.5)






#        if GPIO.input(button3)==1: #Repeat above for button 3
#                print "Button 3 Was Pressed:"
#                Repo.clone_from("https://github.com/veenhof/tom_Project.git", $
#                sleep(.5)
#        else:
#               print("yolo")

