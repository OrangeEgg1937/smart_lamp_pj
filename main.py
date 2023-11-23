from motor import *
import time

# demo test for motor module
if __name__ == '__main__':
    # create the motor object
    motor1 = motor(12)
	
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
