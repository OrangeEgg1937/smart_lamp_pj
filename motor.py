# define the motor class
import time

# define the pwm GPIO pins
PWM_GPIO = [11, 12, 13, 18, 19, 32]

class motor:
	# define the PID controller constants
	Kp = 0.0
	Ki = 0.0
	Kd = 0.0
	isPIDControl = False

	def __init__(self, outputGPIO, frequency, GPIO):
		if outputGPIO not in PWM_GPIO:
			raise ValueError('Invalid GPIO pin for PWM: ' + str(outputGPIO))

		# set the GPIO mode to board
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(outputGPIO, GPIO.OUT)

		# set the frequency and start the PWM
		self.frequency = frequency
		self.pwm = GPIO.PWM(outputGPIO, frequency)

	def setAngle(self, speed):
		# set the duty cycle
		self.pwm.ChangeDutyCycle(speed)

	def start(self):
		# start the PWM
		self.pwm.start(0)

	def stop(self):
		# stop the PWM
		self.pwm.stop()

	# define the PID controller
	def setPID(self, Kp, Ki, Kd):
		self.Kp = Kp
		self.Ki = Ki
		self.Kd = Kd
		self.isPIDControl = True
	
	# disable the PID controller
	def disablePID(self):
		self.isPIDControl = False
