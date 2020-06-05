#Python3

##########  			IMPORTING PACKAGES   			##########

import cv2
import time
import numpy as np
import glob
import os
import datetime
from random import *
from collections import OrderedDict


######	Directory with images verify
img_dir = '/Users/belindabrown/Desktop/Video_Recognition/VdstoVerify/'
##### Accesing path
data_path = os.path.join(img_dir,'*.mp4')
#####  Englobing data
files = glob.glob(data_path)
print("Amount of videos that is going to be analized:			", len(files))
######	Analyzing all the images in the folder
for v1 in files:
	print("\n", v1)
	# Start default camera
	video = cv2.VideoCapture(v1)
	fps = video.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
	frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
	duration = frame_count/fps

	print('Frames per second  = ' + str(fps))
	print('Number of frames estimated in the video = ' + str(frame_count))
	print('Duration del video = ' + str(duration))
	minutes = int(duration/60)
	s = duration%60
	print('Duration in munutes/seconds = ' + str(minutes) + ':' + str(s))
	round_s = round(float(s))
	print("Round seconds ", round_s)
	# Obtaining frame
	ret, frame = video.read()
	img_counter = 0
	frame_set = []
	past = 0
	# Ask the user number of frames per second
	ps = int(input("Enter every few seconds to take a picture of the video:           "))
	# Seconds passed in less than the total of seconds
	while past <= round_s:
		# If seconds passed are 0 (begin) or greater equal
		# of duration requiered for take picture
		if (past == 0) or (past >= ps):
			# System operation time
			os_t = time.time()
			# Round system operation time
			os_tr = round(os_t)
			print("Time passed", past)
			for_name = str(img_counter) + str(past) +str(os_tr)
			img_name = "{}.png".format(for_name)
			img = cv2.resize(frame, (4160, 3120))
			cv2.imwrite('/Users/belindabrown/Desktop/Video_Recognition/FramestoVerify/%s.jpg'%for_name, img)
			print("Image name: {}".format(for_name))
			img_counter = img_counter + 1
		past = past + ps
	# Release each video
	video.release()
