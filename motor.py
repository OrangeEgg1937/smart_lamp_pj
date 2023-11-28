# define the motor class
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

factory = PiGPIOFactory()

def m_bound(x, lower = -90, upper = 90):
	if x < lower:
		return lower
	if x > upper:
		return upper
	return x

class motor:
	# define the PID controller constants
	isPIDControl = False

	def __init__(self, outputGPIO):
		# BECARE THE GPIO IS NOT THE PHYSICAL LOCATION 
		# set the servo motor
		self.currentAngle = 0
		self.servo = Servo(outputGPIO, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
		self.servo.value = self.currentAngle/180

	def setAngle(self, angle):
		# set the duty cycle
		self.currentAngle += angle
		self.servo.value = m_bound(angle)/180
		print(self.servo.value)
