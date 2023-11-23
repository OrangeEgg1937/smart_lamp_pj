from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

print("Start in the middle")

while 1:
	for values in range(-180, 180, 60):
		servo.value=values/180
		sleep(2)
