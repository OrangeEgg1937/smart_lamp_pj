import RPi.GPIO as GPIO
from motor import *
import time

# demo test for motor module
if __name__ == '__main__':
    # create the motor object
    motor1 = motor(12, 50, GPIO)
    
    # start the motor
    motor1.start()
    print(motor1.pwm)
    # set the speed to 0
    motor1.setAngle(0)

    print("Wait for 2s")
    
    time.sleep(2)
    
    duty = 2
    
    while duty <= 12:
        motor1.setAngle(duty)
        time.sleep(1)
        duty +=1
        print("Looping")

    # wait for 5 seconds
    time.sleep(5)
	
    print("User mode")
	
    while True:
        angle = float(input('Enter angle between 0&180: '))
        motor1.setAngle(angle)
        time.sleep(2)
    
    time.sleep(2)
	
    # stop the motor
    motor1.stop()

    # clean up the GPIO
    GPIO.cleanup()
