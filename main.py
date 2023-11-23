import RPi.GPIO as GPIO
import motor
import time

# demo test for motor module
if __name__ == '__main__':
    # set the GPIO mode to board
    GPIO.setmode(GPIO.BOARD)

    # create the motor object
    motor1 = motor(12, 100)

    # start the motor
    motor1.start()

    # set the speed to 0
    motor1.setSpeed(0)

    # wait for 5 seconds
    time.sleep(5)

    # set the speed to 50
    motor1.setSpeed(50)

    # wait for 5 seconds
    time.sleep(5)

    # set the speed to 100
    motor1.setSpeed(100)

    # wait for 5 seconds
    time.sleep(5)

    # set the speed to 0
    motor1.setSpeed(0)

    # wait for 5 seconds
    time.sleep(5)

    # stop the motor
    motor1.stop()

    # clean up the GPIO
    GPIO.cleanup()