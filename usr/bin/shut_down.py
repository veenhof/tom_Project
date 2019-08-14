import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#from git import Repo
from subprocess import call

button1 = 20    #6
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
button2 = 24
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


while(1):                  # Create an infinite Loop
    if GPIO.input(button1)==1 and GPIO.input(button2)==0: #Repeat above for button 2
        print("Button 1 and2 Was Pressed:")
        sleep(3.0)
        if GPIO.input(button2)==0 and GPIO.input(button2)==0:
            print("shutting Down")
            call("sudo shutdown -h now", shell=True)
#    else:
