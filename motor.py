import RPi.GPIO as GPIO
import time

class motor:
	def __init__(self, outputGPIO, frequency):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(outputGPIO, GPIO.OUT)
		
