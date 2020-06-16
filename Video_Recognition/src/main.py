#Python3


##--------------------------------Main file------------------------------------
##
## Copyright (C) 2020 by Belinda Brown Ramírez (belindabrownr04@gmail.com)
##	Image recognition system for diagnosis of a network switch
##
##-----------------------------------------------------------------------------



##########  			IMPORTING PACKAGES   			##########

import cv2
import numpy as np
import glob
import os
from collections import OrderedDict

##########  			DEFINITIONS OF NECESSARY FUNCTIONS   			##########

######					 FILTERING NOISE / MAKING THE IMAGE SHARP
# def denoising_sharpening(input):
#     without_noise= cv2.fastNlMeansDenoisingColored(input, None,15,15,7,15)
#     kernel=np.array([[-1,-1,-1,-1,-1],
#                       [-1,2,2,2,-1],
#                       [-1,2,8,2,-1],
#                       [-2,2,2,2,-1],
#                       [-1,-1,-1,-1,-1]])/8.0
#     without_noise = cv2.filter2D(without_noise,-1,kernel)
#     return without_noise

#### For list items
def mean_arit_list(list):
	n = len(list)
	sum = 0
	for ind in range (0, n):
		sum = sum + list[ind]
	return sum/n

def varnc_list(list):
	n = len(list)
	sum = 0
	for ind in range (0, n):
		sum = sum + (mean_arit_list(list)-list[ind])**2
	return sum/n

def stddesv_list(list):
	desvi = varnc_list(list)**(1/2)
	return desvi

def color_filter(colorlocation, w_color, h_color, image, color):
			#######    FOR COLOR    #####
	######	COMPARING  X
	color_x = []
	y_color_bf = []
	######	COMPARING Y
	color_y = []
	x_color_bf = []
	######	THE FILTERED COLOR COORDINATES
	x_color_f =[]
	y_color_f =[]
	###	TO JOIN THE TWO COLOR VECTORS
	color_flrd_cor = []
	######	Number of LEDs in state # XXX
	num_leds_color = 0
	if len(colorlocation[0]) > 0:
		##### for Y on color before filtered
		for itercolory in sorted(colorlocation[0]):
			if itercolory not in color_y:
				color_y.append(itercolory)
			####	Compying the vector without repetitions to generate the second to compare
			y_color_bf =  color_y.copy()
			####	Obtaining the first coordinate
			y0_color = color_y[0]
			####	Deleting the first coordinate
			y_color_bf.pop(0)
			#### 	The deleted coordinate is added to the result
			y_color_f.append(y0_color)
			#####	Color before filtering for X - basically vector obtained minus repeated coordinates
			for itercolorx in sorted(colorlocation[1]):
				if itercolorx not in color_x:
					color_x.append(itercolorx)
			####	Compying the vector to generate the second
			x_color_bf =  color_x.copy()
			####	Gets the first coordinate obtained from the list of elements without repetitions
			x0_color = color_x[0]
			###		Deleting the first element to be able to subtract with the complete list
			x_color_bf.pop(0)
			###		The deleted coordinate is added to the result
			x_color_f.append(x0_color)
		#### Applying the same method for filter similar Y COORDENATES
		for eee,iii in sorted(zip(color_y,y_color_bf)):
			diff_y_color = iii - eee
			if h_orange < abs(diff_y_color):
				y_color_f.append(iii)
		y_color_f = list(OrderedDict.fromkeys(y_color_f))
		#### Applying the same method for filter similar X COORDENATES
		for eeee,iiii in sorted(zip(color_x,x_color_bf)):
			diff_x_color = iiii - eeee
			if w_orange < abs(diff_x_color):
				x_color_f.append(iiii)
		x_color_f = list(OrderedDict.fromkeys(x_color_f))
		#### counting the total of coordinates finally filtered
		nun_x_color = len(x_color_f)
		nun_y_color = len(y_color_f)
		how_many_color = 0
		while how_many_color < nun_x_color-1 :
			how_many_color = how_many_color +1
			if nun_y_color != nun_x_color and nun_y_color < nun_x_color:
				y_color_f.append(y0_color)
		######		Joining the two x, y coordinates
		color_flrd_cor = sorted(zip(x_color_f, y_color_f))
		for ptcolor in color_flrd_cor:
			####	cv2.rectangle(image where draw, place , color BGR, thick line drawing)
			cv2.rectangle(image, ptcolor, (ptcolor[0] + w_color, ptcolor[1] + h_color), (0,255,255), 4)
			###	In this function the color goes BGR, what it does is put the text where it found the led
			cv2.putText(image, str(color), ptcolor, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 4)
			##### 	Count the number of LEDs you found in this state
			num_leds_color = num_leds_color +1
		print("The number of LEDs in " + color + " status (on / on) found is:      ", num_leds_color)
		return x_color_f

def port_filter(port_location, w_p, h_p, image, name):
		#######    FOR PORT     #####
	port_x = []
	port_x_bff = []
	# 		Port compare Y values
	port_y = []
	port_y_bff = []
	# 		Port coordenates filtered
	port_x_f =[]
	port_y_f =[]
	## Join the coordenates
	port_fil = []
	# Count ports
	count_port = 0

	####    				IF PORT EXIST ...
	if len(port_location[0]) > 0:
		##### Ports X coordenates without repeats
		for i in sorted(port_location[0]):
			if i not in port_x:
				port_x.append(i)
		#### Before filtered x coordinate
		port_x_bff =  port_x.copy()
		#### Obtaining X first coordinate
		x0 = port_x[0]
		#### Deleting the first coordinate
		port_x_bff.pop(0)
		# Append the firt coordinate deleted before to the coordenates filtered
		port_x_f.append(x0)
		#### Before filtered y coordinate
		for j in sorted(port_location[1]):
			if j not in port_y:
				port_y.append(j)
		#### Before filtered y coordinate
		port_y_bff =  port_y.copy()
		#### Obtaining Y first coordinate
		y0 = port_y[0]
		#### Deleting the first coordinate
		port_y_bff.pop(0)
		# Append the firt coordinate deleted before to the coordenates filtered
		port_y_f.append(y0)
		#### To automate the filtering, the dispersion measures are calculated
		port_x_mean = mean_arit_list(port_x)
		#print("Port mean x coordinates		", port_x_mean)
		port_x_var = varnc_list(port_x)
		#print("Port variance x coordinates 	", port_x_var)
		port_x_stdesv = stddesv_list(port_x)
		#print("Port standard deviation x coordinates 	", port_x_stdesv)
		port_y_mean = mean_arit_list(port_y)
		port_y_stdesv = stddesv_list(port_y)
		#### Applying the same method for filter similar X COORDENATES
		for nne,nni in sorted(zip(port_x,port_x_bff)):
			sub_port_x = nni - nne
			if abs(port_x_stdesv) <abs(sub_port_x):
				port_x_f.append(nni)
		port_x_f = list(OrderedDict.fromkeys(port_x_f))
		#### Applying the same method for filter similar Y COORDENATES
		for nnee,nnii in sorted(zip(port_y,port_y_bff)):
			Resta_Y_NN = nnii - nnee
			if abs(port_y_mean - port_y_stdesv) < abs(Resta_Y_NN):
				port_y_f.append(nnii)
		port_y_f = list(OrderedDict.fromkeys(port_y_f))
		##### Counting the total of coordinates finally filtered
		count_port_x = len(port_x_f)
		count_port_y = len(port_y_f)
		count_p = 0
		while count_p < count_port_y-1 :
			count_p = count_p +1
			if count_port_x != count_port_y and count_port_x < count_port_y:
				port_x_f.append(x0)
		loc_leds = []
		loc_to_add = 0
		for i in port_y_f:
			loc_to_add = i + w_p -100
			loc_leds.append(loc_to_add)
		loc_leds = list(OrderedDict.fromkeys(loc_leds))
		loc_full_port = []
		# Concatenate port positions
		loc_full_port = sorted(port_y_f + loc_leds )
		# Port_fil will have the coordenates as ordered pairs
		port_fil = sorted(zip(port_y_f, port_x_f))
		# Drawing ports id on images
		for pix_port in port_fil:
			#### Rectangle and colors as color BGR
			cv2.rectangle(image, pix_port, (pix_port[0] + w_p, pix_port[1] + h_p), (0,255,255), 5)
			#### Label on drawing
			cv2.putText(image, str(name), pix_port, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 5)
			###  Count port template, in each template are two ports. Thats why count_port*2
			count_port = count_port + 1
		print("The number of ports are:      ", count_port*2)
		return loc_full_port

######	Read the template
template_green = cv2.imread('',0)
template_orange = cv2.imread('',0)
template_dark_orange = cv2.imread('',0)
template_port = cv2.imread('',0)

######	Store the width (w) and height (h) of the template
w_green, h_green = template_green.shape[::-1]
w_orange, h_orange = template_orange.shape[::-1]
w_dark_orange, h_dark_orange = template_dark_orange.shape[::-1]
w_port, h_port = template_port.shape[::-1]

######	Specifying (threshold)
threshold= 0.9
thresholdport= 0.515

######	Directory with images verify
img_dir = ''
data_path = os.path.join(img_dir,'*.jpg')
files = glob.glob(data_path)
data = []
######	Analyzing all the images in the folder
for f1 in sorted(files):

	##### Read each image
	img = cv2.imread(f1)
	print("\n", f1) #picture name

	##### Store image data
	data.append(img)
	#####	uses a gray filter for easy recognition
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, 0)

	########		 COMPARING THE IMAGE USING TEMPLATE METHOD 			########
	res_matching_green = cv2.matchTemplate(img_gray,template_green,cv2.TM_CCOEFF_NORMED)
	res_matching_orange = cv2.matchTemplate(img_gray,template_orange,cv2.TM_CCOEFF_NORMED)
	res_matching_dark_orange = cv2.matchTemplate(img_gray,template_dark_orange,cv2.TM_CCOEFF_NORMED)
	res_matching_port = cv2.matchTemplate(img_gray,template_port,cv2.TM_CCOEFF_NORMED)

	##### If you use denoising image:
	#f1Filtered = cv2.imread(f1)
	#img = denoising_sharpening(f1Filtered)

	###### Announces every time an image is reviewed
	print("Image loaded, analyzing patterns ...")
	###### Gets the position of matching
	location_green = np.where(res_matching_green >= threshold)
	location_orange = np.where(res_matching_orange >= threshold)
	location_dark_orange = np.where(res_matching_dark_orange >= threshold)
	location_port = np.where(res_matching_port >= thresholdport)
	# Calling functions
	X_Green_Filtered0 = color_filter(location_green, w_green, h_green, img, 'GREEN')
	X_YellowOrange_Filtered0 = color_filter(location_orange, w_orange, h_orange, img, 'ORANGE')
	X_OrangeOrange_Filtered0 = color_filter(location_dark_orange, w_dark_orange, h_dark_orange, img, 'DARK ORANGE')
	loc_full_port0 = port_filter(location_port, w_port, h_port, img, 'PORT')

	# Checking empty
	if X_Green_Filtered0:
		X_Green_Filtered = list(OrderedDict.fromkeys(X_Green_Filtered0))
	else:
		X_Green_Filtered = []

	if X_YellowOrange_Filtered0:
		X_YellowOrange_Filtered = list(OrderedDict.fromkeys(X_YellowOrange_Filtered0))
	else:
		X_YellowOrange_Filtered = []

	if X_OrangeOrange_Filtered0:
		X_OrangeOrange_Filtered = list(OrderedDict.fromkeys(X_OrangeOrange_Filtered0))
	else:
		X_OrangeOrange_Filtered = []

	if loc_full_port0:
		loc_full_port = list(OrderedDict.fromkeys(loc_full_port0))
	else:
		loc_full_port = []

	leds_on_fnd = sorted(list(OrderedDict.fromkeys(X_YellowOrange_Filtered + X_Green_Filtered + X_OrangeOrange_Filtered)))

	print("Positions of the leds ON found", leds_on_fnd)
	number_label = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11 ,12]
	loc_led_templ = sorted(zip(loc_full_port,number_label))
	diff = [] # For the result of the sub created for filter positions
	for i in sorted(loc_led_templ):
		for j in sorted(leds_on_fnd):
			z = j + 20
			x = i[0] - z
			if x in range(-150,70):
				if j in X_Green_Filtered:
					print("Port", i[1], "status:						Green")
				elif j in X_YellowOrange_Filtered:
					print("Port", i[1], "status:						Orange")
				elif j in X_OrangeOrange_Filtered:
					print("Port", i[1], "status:						Dark Orange")
	# #### Shows me the figure already analyzed
	cv2.imshow("\nProcessed Image",img)
	### Since there are several, wait until you press a key and thus analyze the other image
	cv2.waitKey(0)
### Once finished remove all windows
cv2.destroyAllWindows()
