from motor import *
from light_sensor import *
import time

# demo test for motor module
if __name__ == '__main__':
    # create a light sensor object
    light = light_sensor(16)
	
    print("Iight sensor test:")
	
    while True:
        print("Current light: ", light.getLight())
        time.sleep(2)
    
    time.sleep(2)
	
    # stop the motor
    motor1.stop()

    # clean up the GPIO
    GPIO.cleanup()
