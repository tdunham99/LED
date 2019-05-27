import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
LEDPin = 22
LEDPin2 = 23

# Setup the pin that the LED is connected to 
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(LEDPin2, GPIO.OUT)

try:
	while count < blinkCount:
		GPIO.output(LEDPin, True)
		GPIO.output(LEDPin2, False)
		print("LED ON")
		sleep(3)
		GPIO.output(LEDPin, False)
		GPIO.output(LEDPin2, True)
		print("LED OFF")
		sleep(3)
		count += 1

finally:
	GPIO.cleanup()
