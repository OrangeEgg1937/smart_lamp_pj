import RPi.GPIO as GPIO

class light_sensor:
    def __init__(self, inputGPIO):
        self.inputGPIO = inputGPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.inputGPIO, GPIO.IN)

    # detect light will output 0
    def getLight(self):
        return GPIO.input(self.inputGPIO)
