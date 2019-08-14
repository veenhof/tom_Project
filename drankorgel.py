import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#from git import Repo

button1 = 20    #6
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button2 = 24
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


relay1= 17
GPIO.setup(17, GPIO.OUT)
relay2= 23
GPIO.setup(23, GPIO.OUT)
relay3= 27
GPIO.setup(27, GPIO.OUT)
relay4= 22

while(1):                  # Create an infinite Loop
    if GPIO.input(button1)==1:            # Look for button 1 press
        print("Button 1 Was Pressed:")
        GPIO.output(relay1,True) # turn it on
        sleep(3.5)             # Delay
        GPIO.output(relay1,False)
        GPIO.output(relay2,True) # turn it on
        sleep(8.5)
        GPIO.output(relay2,False) # Turn relay 2 off

    else:                         # If the LED is on
        GPIO.output(relay1,False) # Turn relay 1 off
        GPIO.output(relay2,False) # Turn relay 2 off
    if GPIO.input(button2)==0: #Repeat above for button 2
       print("Button 2 Was Pressed:")
       GPIO.output(relay3,True)
       sleep(3.5)
       GPIO.output(relay3,False)
        GPIO.output(relay4,True)
       sleep(8.5)
       GPIO.output(relay3,False)
    else:
        GPIO.output(relay3,False)
        GPIO.output(relay4,False)
#        if GPIO.input(button3)==1: #Repeat above for button 3
#                print "Button 3 Was Pressed:"
#                Repo.clone_from("https://github.com/veenhof/tom_Project.git", $
#                sleep(.5)
#        else:
#               print("yolo")

