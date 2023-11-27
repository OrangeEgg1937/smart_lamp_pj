# require library
# sudo pip3 install rpi_ws281x 
# sudo pip3 install adafruit-circuitpython-neopixel
# sudo python3 -m pip install --force-reinstall adafruit-blinka

# define the led_matrix class

# # define the pwm GPIO pins
# PWM_GPIO = [11, 12, 13, 18, 19, 32]

# class motor:
# 	# define led matrix constants
# 	length = 0
	
# 	def __init__(self, outputGPIO):
# 		if outputGPIO not in PWM_GPIO:
# 			raise ValueError('Invalid GPIO pin for PWM: ' + str(outputGPIO))

# 		# set the servo motor
# 		self.servo = Servo(outputGPIO, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

# 	def setAngle(self, angle):
# 		# set the duty cycle
# 		servo.value = angle/180

from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 20      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

for x in range(0,LED_COUNT):
    strip.setPixelColor(x,Color(255,0,0))

strip.show()
