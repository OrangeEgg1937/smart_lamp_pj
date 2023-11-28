from light_sensor import *
from motor import *
import time

# demo test for motor module
if __name__ == '__main__':
    # create a light sensor object
    motor_rotate = motor(13)
    print("Iight sensor test:")
    time.sleep(3)
    motor_rotate.setAngle(-90)
    time.sleep(3)
    motor_rotate.setAngle(90)
    while True:
        current = 0
        
    
    # set angle to 1
    # motor_rotate.setAngle(1)
    
    
    time.sleep(2)
	

    # clean up the GPIO
    GPIO.cleanup()
