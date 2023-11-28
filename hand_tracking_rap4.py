import mediapipe as mp
from picamera2 import Picamera2
import cv2
import numpy as np
import threading
import time
import board
import neopixel
from motor import *
from light_sensor import *

# Connection of the project
# LED matrix: GPIO18 (pin 12)
# Motor: GPIO13 (pin 33), GPIO19 (pin 35), GPIO26 (pin 37), GPIO16 (pin 36)
# Light sensor: GPIO16 (pin 36)
# picamera2 version

class VideoCaptureThread(threading.Thread):
    def __init__(self):
        super(VideoCaptureThread, self).__init__()
        self.cam = Picamera2()
        self.cam.configure(self.cam.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        self.cam.start()
        self.frame = None
        self.running = True

    def run(self):
        while self.running:
            self.frame = self.cam.capture_array()


    def stop(self):
        self.running = False
        self.join()
        
def get_guester(img,list_lms):

    hull_index = [0,1,2,3,6,10,14,19,18,17]
    hull = cv2.convexHull(list_lms[hull_index,:])

    cv2.polylines(img,[hull], True, (0, 255, 0), 2)

    n_fig = -1
    ll = [4,8,12,16,20] 
    up_fingers = []
    
    for i in ll:
        pt = (int(list_lms[i][0]),int(list_lms[i][1]))
        dist= cv2.pointPolygonTest(hull,pt,True)
        if dist <0:
            up_fingers.append(i)
            
    guester = None
    
    if len(up_fingers)==1 and up_fingers[0]==8:
        guester = 1
    elif len(up_fingers)==2 and up_fingers[0]==8 and up_fingers[1]==12:
        guester = 2

    elif len(up_fingers)==3 and up_fingers[0]==8 and up_fingers[1]==12 and up_fingers[2]==16:
        guester = 3
     
    elif len(up_fingers)==4 and up_fingers[0]==8 and up_fingers[1]==12 and up_fingers[2]==16 and up_fingers[3]==20:
        guester = 4
        
    elif len(up_fingers)==5:
        guester = 5
        
    elif len(up_fingers)==2 and up_fingers[0]==4 and up_fingers[1]==20:
        guester = 6  
    elif len(up_fingers)==2 and up_fingers[0]==4 and up_fingers[1]==8:
        guester = 8
    
    elif len(up_fingers)==0:
        guester = 10
    
    return guester

def bound(x, upper = 0.0, lower = 1.0):
	if x > upper:
		x = upper
	elif x < lower:
		x = lower
	return x

if __name__ == "__main__":

	# creating a video capture thread
	thread = VideoCaptureThread()
	thread.start()
	
	# Import the hand related library fomr mediapipe
	mpHand = mp.solutions.hands
	hands = mpHand.Hands()
	mpDraw = mp.solutions.drawing_utils
	
	# set guester code
	c_guester = None
	
	# set the central position
	c_x = 0
	c_y = 0
	c_x_UpperBound = 310
	c_x_LowerBound = 180
	c_y_UpperBound = 290
	c_y_LowerBound = 230
	
	# declear the LED matrix
	led_matrix = neopixel.NeoPixel(board.D18, 20, brightness=1)
	# color parameters
	red = 255
	green = 255
	blue = 255
	bightness = 1.0
	#led_matrix.fill((red * bightness, green * bightness, blue * bightness)) # turn off all LEDs
	isLightOn = True # whether the light is on or off
	
	# declear light sensor
	light = light_sensor(16)
	currentLight = light.getLight()
	isAlwaysOnSensor = True
	
	# declear timeout variables
	isNotTimeout = True 

	while True:
		pos_text = ""
		
		# get the light sensor result
		currentLight = light.getLight()
		
		# process the LED matrix
		if (isLightOn & (currentLight & isAlwaysOnSensor)) & isNotTimeout:
			print("TurnOnLED")
			print("RED: ", red, " Green", green, " Blue:", blue)
			led_matrix.fill((red * bightness, green * bightness, blue * bightness))
		else:
			print("TurnOffLED")
			led_matrix.fill((0,0,0))

		# Get one frame
		img = thread.frame
		
		if img is None:
			continue
		
		img = cv2.rotate(img, 2)
		image_height, image_width, _ = np.shape(img)
		# change the color for mediapipe input
		imgRGB = cv2.cvtColor(img, 4)
		results = hands.process(imgRGB)
		
		if results.multi_hand_landmarks:
			for hand in results.multi_hand_landmarks:
				list_lms = []
				for i in range(21):
					pos_x = hand.landmark[i].x*image_width
					pos_y = hand.landmark[i].y*image_height
					list_lms.append([int(pos_x),int(pos_y)])
					cv2.circle(img, (int(pos_x),int(pos_y)), 3, (0,255,255), -1)
					if i == 1:
						c_x = pos_x
						c_y = pos_y
						pos_text = str(int(pos_x)) + "," + str(int(pos_y))
					
				# Get the guester
				list_lms = np.array(list_lms,dtype=np.int32)
				c_guester = get_guester(img, list_lms)

		else:
			c_x = 0
			c_y = 0
			c_guester = 0
		
		action_text = ""
		moving_text = ""
		
		if (c_x < c_x_LowerBound) & (c_x != 0):
			action_text += "x=R:"
		elif c_x > c_x_UpperBound:
			action_text += "x=L:"	


		if (c_y < c_y_LowerBound) & (c_y != 0):
			action_text += "y=U:"
		elif c_x > c_y_UpperBound:
			action_text += "y=D:"
			
			
		print(pos_text)
		
		if c_guester == 1:
			action_text = "Light on"
			isLightOn = True
		elif c_guester == 2:
			action_text = "Light off"
			isLightOn = False
		elif c_guester == 3:
			action_text = "Brightness up"
			bightness = bound(bightness + 0.1)
		elif c_guester == 4:
			action_text = "Brightness down"
			bightness = bound(bightness - 0.1)
		elif c_guester == 5:
			action_text = "Stop sleep mode"
		elif c_guester == 6:
			action_text = "Switch Color"
			if red == 255 & green == 255 & blue == 255:
				red = 255
				green = 0
				blue = 0
			elif red == 255:
				red = 0
				green = 255
			elif green == 255:
				green = 0
				blue = 255
			elif blue == 255:
				print("now is blue")
				red = 255
				green = 255
				blue = 255
		elif c_guester == 8:
			action_text = "Action 6"
		elif c_guester == 10:
			action_text = "Action 7"		
		
		# According user action to process	
		img = cv2.putText(img, text=action_text, org=(150, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
		img = cv2.putText(img, text=moving_text, org=(0, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(255, 0, 0),thickness=3)
		img = cv2.putText(img, text=pos_text, org=(30, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=3)
		
		cv2.imshow("hands", img)
		
		key = cv2.waitKey(1) & 0xFF
		
		if key == ord('q'):
			break

thread.stop()
