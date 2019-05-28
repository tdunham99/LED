import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
yellow = 22
green = 17
red = 12
blue = 21

# Setup the pin that the LED is connected to
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
try:
        while count < blinkCount:
                GPIO.output(yellow, True)
                GPIO.output(green, False)
		GPIO.output(red, True)
		GPIO.output(blue, False)
                print("GROUP 1 ON")
                sleep(2)
                GPIO.output(yellow, False)
                GPIO.output(green, True)
		GPIO.output(red, False)
		GPIO.output(blue, True)
                print("Group 2 ON")
                sleep(2)
                count += 1

finally:
        GPIO.cleanup()