import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Liquor pumps sleeptime     hoe lang draait het alcahol pompje?
SleepTime = 2
#Soda Pumps Sleeptime
SleepTimeSoda = 10

#Button 1
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Button 2
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Button 3
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#while True: # Run forever
if GPIO.input(4) > 0:
    print("Knop 1 pushed, BACO!")
elif GPIO.input(7) > 0:
    print("Knop 2 pushed, Wodka jus!")
elif GPIO.input(22) > 0:
    print("Knop 2 pushed, UPDATE!")
    Repo.clone_from("https://github.com/veenhof/tom_Project.git", "tom_Project")
