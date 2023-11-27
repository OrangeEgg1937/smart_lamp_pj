# define the motor class
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

factory = PiGPIOFactory()

# define the pwm GPIO pins
PWM_GPIO = [11, 12, 13, 18, 19, 32]

class motor:
	# define the PID controller constants
	Kp = 0.0
	Ki = 0.0
	Kd = 0.0
	isPIDControl = False

	def __init__(self, outputGPIO):
		if outputGPIO not in PWM_GPIO:
			raise ValueError('Invalid GPIO pin for PWM: ' + str(outputGPIO))
		# BECARE THE GPIO IS NOT THE PHYSICAL LOCATION 
		# set the servo motor
		self.servo = Servo(outputGPIO, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

	def setAngle(self, angle):
		# set the duty cycle
		self.servo.value = angle/180
