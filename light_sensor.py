import RPi.GPIO as GPIO

class light_sensor:
    def __init__(self, inputGPIO):
        self.inputGPIO = inputGPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.inputGPIO, GPIO.IN)

    def getLight(self):
        return GPIO.input(self.inputGPIO)