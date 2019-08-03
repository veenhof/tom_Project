import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
from git import Repo

button1=21
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button2=20
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button3=16
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

relay1=25
GPIO.setup(25, GPIO.OUT)
relay2=26
GPIO.setup(26, GPIO.OUT)
relay3=27
GPIO.setup(27, GPIO.OUT)
relay4=28
GPIO.setup(28, GPIO.OUT)

while(1):                  # Create an infinite Loop
        if GPIO.input(button1)==1:            # Look for button 1 press
                print "Button 1 Was Pressed:"
                GPIO.output(relay1,True) # turn it on
                sleep(.5)             # Delay
                GPIO.output(relay2,True) # turn it on
                sleep(.5)
        else:                         # If the LED is on
                GPIO.output(relay1,False) # Turn relay 1 off
                GPIO.output(relay2,False) # Turn relay 2 off
                sleep(.5)
        if GPIO.input(button2)==1: #Repeat above for button 2
                print "Button 2 Was Pressed:"
                GPIO.output(relay3,True)
                GPIO.output(relay4,True)
                sleep(.5)
        else:
                GPIO.output(relay3,False)
                sleep(.5)
        if GPIO.input(button3)==1: #Repeat above for button 3
                print "Button 3 Was Pressed:"
                Repo.clone_from("https://github.com/veenhof/tom_Project.git", "tom_Project")
                                sleep(.5)
        else:
                GPIO.output(relay4,False)
                sleep(.5)
