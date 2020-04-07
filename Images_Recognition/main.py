#Python3

##########  			IMPORTING PACKAGES   			##########

import cv2
import numpy as np
import glob
import os
from collections import OrderedDict

##########  			DEFINITIONS OF NECESSARY FUNCTIONS   			##########

######					 FILTERING NOISE / MAKING THE IMAGE SHARP
#####   Using Kittler's thresholding using the
#####   tool previously created in  https://github.com/brown9804/Image_Segmentation_Project-
#####   a variance of 1: 15.381974 is obtained, so values ​​are used 15 for images
#####	since they are considered to be laboratory without changes in lighting
#####	Considering the different tests, the values ​​are considered
####	15 15 7 15 (30s approx) although
#####	the bibliography read recommends values ​​of 10 10 7 21 (1:42 minutess approx)

# def denoising_sharpening(input):
#     sin_ruido= cv2.fastNlMeansDenoisingColored(input, None,15,15,7,15)
#     kernel=np.array([[-1,-1,-1,-1,-1],
#                       [-1,2,2,2,-1],
#                       [-1,2,8,2,-1],
#                       [-2,2,2,2,-1],
#                       [-1,-1,-1,-1,-1]])/8.0
#     sin_ruido = cv2.filter2D(sin_ruido,-1,kernel)
#     return sin_ruido

###### We define a function that calculates the arithmetic mean of the elements of the list.
###### Calculates the average value of all numbers, adds all and divides them by the total amount

# def media_arit(list):
#     n = float(len(list))
#     return tuple(sum(x[i] for x in list)/n for i in range (len(list[0])))

#####	We define a function for variance between the elements of the list
#####	the square of the standard deviation, defined below the standard deviation.

# def varianza(list):
#     n = float(len(list))
#     return tuple(sum(x[i] + (media_arit(list)-x[i])**2   for x in list)/n for i in range (len(list[0])))


####   For a list
#### Arithmetic average
def ArithmeticAveragelist(list):
	n = len(list)
	sum = 0
	for indice in range (0, n):
		sum = sum + list[indice]
	return sum/n
####	Variance
def variance_list(list):
	n = len(list)
	sum = 0
	for indice in range (0, n):
		sum = sum + (ArithmeticAveragelist(list)-list[indice])**2
	return sum/n

####	Standard deviation
##	Standard deviation is the most common measure of dispersion, indicating how
## scattered the data is with respect to average. The greater the standard deviation,
##	the greater will be the dispersion of the data. We need it because it doesn't
## consider very abrupt changes in pixel values, as well as their location greater than zero.
def StandarDesv(list):
	desvi = variance_list(list)**(1/2)
	return desvi


######	Read the template
template_green = cv2.imread('',0)
template_orange = cv2.imread('',0)
template_dark_orange = cv2.imread('',0)

######	Store the width (w) and height (h) of the template
w_green, h_green = template_green.shape[::-1]
w_orange, h_orange = template_orange.shape[::-1]
w_dark_orange, h_dark_orange = template_dark_orange.shape[::-1]

######	Specifying (threshold)
threshold= 0.92
######	Directory with images verify
img_dir = ''
data_path = os.path.join(img_dir,'*.jpg')
files = glob.glob(data_path)
data = []
######	Analyzing all the images in the folder
for f1 in files:
					########   FOR GREEN     ######
	######	COMPARING  X
	Geen_x = []
	X_Green_before_filtered = []
	######	COMPARING Y
	Green_y = []
	Y_Green_before_filtered = []
	######	THE FILTERED GREEN COORDINATES
	X_Green_Filtered =[]
	Y_Green_Filtered =[]
	########	TO JOIN THE TWO GREEN VECTORS
	Green_filtered_coordenates = []
	######	Number of LEDs in state # XXX
	Quantity_Leds_Green = 0
					#######    FOR YELLOW ORANGE    #####
	######	COMPARING  X
	YellowOrange_x = []
	X_YellowOrange_before_filtered = []
	######	COMPARING Y
	YellowOrange_y = []
	Y_YellowOrange_before_filtered = []
	######	THE FILTERED YELLOW ORANGE COORDINATES
	X_YellowOrange_Filtered =[]
	Y_YellowOrange_Filtered =[]
	###	TO JOIN THE TWO GREEN VECTORS
	YellowOrange_filtered_coordenates = []
	######	Number of LEDs in state # XXX
	Quantity_Leds_YellowOrange = 0
					#######    FOR ORANGE ORANGE     #####
	######	COMPARING  X
	OrangeOrange_x = []
	X_OrangeOrange_before_filtered = []
	######	COMPARING  Y
	OrangeOrange_y = []
	Y_OrangeOrange_before_filtered = []
	######	THE FILTERED YELLOW ORANGE COORDINATES
	X_OrangeOrange_Filtered =[]
	Y_OrangeOrange_Filtered =[]
	########	TO JOIN THE TWO GREEN VECTORS
	OrangeOrange_filtered_coordenates = []
	######	Number of LEDs in state # XXX
	Quantity_Leds_OrangeOrange = 0

	##### Read each image
	img = cv2.imread(f1)
	print("\n", f1) #picture name
	##### Store image data
	data.append(img)
	#####	uses a gray filter for easy recognition
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, 0)
	########		 COMPARING THE IMAGE USING TEMPLATE METHOD 			########
	#####	Template Matching is a method to search and find the location of
	###### a template image into a larger image. OpenCV comes with a
	###### function cv2.matchTemplate () for this purpose. Just slide
	###### the template image over the input image (as in 2D convolution)
	###### and compare the template and patch of the input image below the image
	###### Of the template. Various comparison methods are implemented in OpenCV.
	##### Return a grayscale image, where each pixel indicates how much
	##### match the neighborhood of that pixel with the template.

	##### TM_CCOEFF_NORMED does Correlation coefficient: the method is simply used to
	##### a) make the template and image zero and
	##### b) make the dark parts of the image negative values
	##### and the bright parts of the positive values ​​of the image.
	res_matching_green = cv2.matchTemplate(img_gray,template_green,cv2.TM_CCOEFF_NORMED)
	res_matching_orange = cv2.matchTemplate(img_gray,template_orange,cv2.TM_CCOEFF_NORMED)
	res_matching_dark_orange = cv2.matchTemplate(img_gray,template_dark_orange,cv2.TM_CCOEFF_NORMED)

	##### If you use denoising image:
	#f1Filtrada = cv2.imread(f1)
	#img = denoising_sharpening(f1Filtrada)

	###### Announces every time an image is reviewed
	print("Image loaded, analyzing patterns ...")
	###### gets the position
	######-- theoretically
	###### Returns elements chosen from x or y depending on the condition.
	###### gives location x, and separated from all meet the condition
	location_green = np.where(res_matching_green >= threshold)
	location_orange = np.where(res_matching_orange >= threshold)
	location_dark_orange = np.where(res_matching_dark_orange >= threshold)
							########## IF THERE IS GREEN THEN ... ##########
	####### GREEN BEFORE FILTERING for X - without repeats
	if len(location_green[0]) > 0:
		for itergreenx in sorted(location_green[0]):
			if itergreenx not in Geen_x:
				Geen_x.append(itergreenx)
		###### Compying the vector without repetitions to generate the second to compare
		X_Green_before_filtered =  Geen_x.copy()
		######	Obtaining the first coordinate
		xGreen0 = Geen_x[0]
		###### Deleting the first coordinate
		X_Green_before_filtered.pop(0)
		######	The deleted coordinate is added to the result
		X_Green_Filtered.append(xGreen0)
		#####	Green before filtering for y - basically vector obtained minus repeated coordinates
		for itergreeny in sorted(location_green[1]):
			if itergreeny not in Green_y:
				Green_y.append(itergreeny)
		#####	Compying the vector to generate the second
		Y_Green_before_filtered =  Green_y.copy()
		##### Gets the first coordinate obtained from the list of elements without repetitions
		yGreen0 = Green_y[0]
		#######	Deleting the first element to be able to subtract with the complete list
		Y_Green_before_filtered.pop(0)
		######	The deleted coordinate is added to the result
		Y_Green_Filtered.append(yGreen0)
		#####	To automate the filtering, the dispersion measurements are calculated
		X_ArithmeticAverage_Green = ArithmeticAveragelist(Geen_x)
		# print("Arithmetic Average x Green", X_ArithmeticAverage_Green)
		X_Variance_Green = variance_list(Geen_x)
		# print("Variance x Green", X_Variance_Green)
		X_StandarDesv_Green = StandarDesv(Geen_x)
		# print("Standard Desvx Green", X_StandarDesv_Green)
		Y_ArithmeticAverage_Green = ArithmeticAveragelist(Green_y)
		# print("Arithmetic Average y Green", Y_ArithmeticAverage_Green)
		Y_Variance_Green = variance_list(Green_y)
		# print("Variance y Green", Y_Variance_Green)
		Y_StandarDesv_Green = StandarDesv(Green_y)
		# print("Standard Desv y Verde", Y_StandarDesv_Green)
		# print("Green x complete ", Geen_x)
		# print('Green y complete', Green_y)
				########## 						GREEN	COORDENATES FILTERS  									##########
		#Filter for X coordinate, because it locates pixels with similar threshold in the near area
		# That is to say 1678,1679,1680 are 3 consecutive pixels so I would draw 3 rectangles
		#Then for a group of similar data we need a coordinate. Since they don't change as much between
		#groups is indifferent if the first one is not obtained, since the second meets the needs.
		for e, i in sorted(zip(Geen_x, X_Green_before_filtered)):
			Diff_X_Green = i - e
			# print(i)
			# print(e)
			# print("Diff x Green ", Diff_X_Green, i)
			if X_StandarDesv_Green < Diff_X_Green:
				X_Green_Filtered.append(i)
		X_Green_Filtered = list(OrderedDict.fromkeys(X_Green_Filtered))
		# Filter for the Y coordinate, because it locates pixels with a similar threshold in the near area
		# That is,  144,145,146  are 3 consecutive pixels, so I would draw 3 rectangles
		# Then for a group of similar data we need a coordinate. Since they don't change as much between
		# groups is indifferent if the first is not obtained, given that the second meets the needs.
		for ee, ii in sorted(zip(Green_y, Y_Green_before_filtered)):
			Diff_Y_Green = ii - ee
			# print(ii)
			# print(ee)
			# print("Diff_Y_Green", Diff_Y_Green, ii)
			if Y_ArithmeticAverage_Green - Y_StandarDesv_Green < Diff_Y_Green:
				Y_Green_Filtered.append(ii)
		Y_Green_Filtered = list(OrderedDict.fromkeys(Y_Green_Filtered))
		#### Filter for the X coordinate, because it locates pixels with a similar threshold in the near area
		#### Now to be able to order it again in coordinates we need an nxn array
		#### Considering the filtering logic and the architecture at the port level in the switch
		#### We know that given the necessary specifications, there may be a deviation angle, considering
		##### this and the structure of the ports.
		number_X_Green = len(X_Green_Filtered)
		number_Y_Green = len(Y_Green_Filtered)
		# print("ny" , number_Y_Green)
		# print("nx", number_X_Green)
		HowManyGreen = 0
		while HowManyGreen < number_Y_Green-1:
			HowManyGreen = HowManyGreen +1
			# print(HowManyGreen, X_Green_Filtered)
			if number_X_Green != number_Y_Green and number_X_Green < number_Y_Green:
				X_Green_Filtered.append(xGreen0)
		# print("X_Green_Filtered", X_Green_Filtered)
		# print("Y_Green_Filtered", Y_Green_Filtered)
		######		Joining the two x, y coordinates
		Green_filtered_coordenates = sorted(zip(Y_Green_Filtered, X_Green_Filtered))
		######	zip location return  example:  <zip object at 0x11cf638c0> pack and acces
		####	zip () con n arguments, then the function will return an iterator that generates tuples of length n.
		#####	Print points as (x,y)
		# print(" Coordinate pairs for Green_filtered point ",Green_filtered_coordenates)
		###### 	Draw the rectangle in that case where it finds green
		for ptGreen in Green_filtered_coordenates:
			####	cv2.rectangle(image where draw, place , color, thick line drawing)
			###		color BGR
			cv2.rectangle(img, ptGreen, (ptGreen[0] + w_green, ptGreen[1] + h_green), (0,255,255), 4)
			###	In this function the color goes BGR, what it does is put the text where it found the led
			cv2.putText(img, 'GREEN', ptGreen, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 4)
			##### 	Count the number of LEDs you found in this state
			Quantity_Leds_Green = Quantity_Leds_Green +1
		print("The number of LEDs in Green Green status (on / on) found is:      ", Quantity_Leds_Green)
				########## 						YELLOW ORANGE	COORDENATES FILTERS  									##########
	if len(location_orange[0]) > 0:
		##### for x on yellow orange before filtered
		for iteryelloworangX in sorted(location_orange[0]):
			if iteryelloworangX not in YellowOrange_x:
				YellowOrange_x.append(iteryelloworangX)
		####	Compying the vector without repetitions to generate the second to compare
		X_YellowOrange_before_filtered =  YellowOrange_x.copy()
		####	Obtaining the first coordinate
		xYellowOrang0 = YellowOrange_x[0]
		####	Deleting the first coordinate
		X_YellowOrange_before_filtered.pop(0)
		#### 	The deleted coordinate is added to the result
		X_YellowOrange_Filtered.append(xYellowOrang0)
		#####	yellow orange before filtering for y - basically vector obtained minus repeated coordinates
		for iteryelloworangY in sorted(location_orange[1]):
			if iteryelloworangY not in YellowOrange_y:
				YellowOrange_y.append(iteryelloworangY)
		####	Compying the vector to generate the second
		Y_YellowOrange_before_filtered =  YellowOrange_y.copy()
		####	Gets the first coordinate obtained from the list of elements without repetitions
		yYellowOrang0 = YellowOrange_y[0]
		###		Deleting the first element to be able to subtract with the complete list
		Y_YellowOrange_before_filtered.pop(0)
		###		The deleted coordinate is added to the result
		Y_YellowOrange_Filtered.append(yYellowOrang0)
		####	To automate the filtering, the dispersion measurements are calculated
		X_ArithmeticAverage_YellowOrange = ArithmeticAveragelist(YellowOrange_x)
		# print("Arithmetic Average Yellow Orange X ", X_ArithmeticAverage_YellowOrange)
		X_Variance_YellowOrange = variance_list(YellowOrange_x)
		# print("Variance Yellow Orange X ", X_Variance_YellowOrange)
		X_StandarDesv_YellowOrange = StandarDesv(YellowOrange_x)
		# print("Standard Desv Amarillo Naranja X ", X_StandarDesv_YellowOrange)
		Y_ArithmeticAverage_YellowOrange = ArithmeticAveragelist(YellowOrange_y)
		# print("Arithmetic Average Yellow Orange Y", Y_ArithmeticAverage_YellowOrange)
		Y_Variance_YellowOrange = variance_list(YellowOrange_y)
		# print("Variance Yellow Orange Y", Y_Variance_YellowOrange)
		Y_StandarDesv_YellowOrange = StandarDesv(YellowOrange_y)
		# print("Standard Desv Yellow Orange Y ", Y_StandarDesv_YellowOrange)
		# print("Yellow Orange x complete ", YellowOrange_x)
		# print('Yellow Orange y complete', YellowOrange_y)

		#### Applying the same method for filter similar X COORDENATES
		for eee,iii in sorted(zip(YellowOrange_x,X_YellowOrange_before_filtered)):
			Diff_X_YellowOrnge = iii - eee
			# print("Diff x Yellow Orange", Diff_X_YellowOrnge, iii)
			if X_StandarDesv_YellowOrange<Diff_X_YellowOrnge:
				X_YellowOrange_Filtered.append(iii)
		X_YellowOrange_Filtered = list(OrderedDict.fromkeys(X_YellowOrange_Filtered))

		#### Applying the same method for filter similar Y COORDENATES
		for eeee,iiii in sorted(zip(YellowOrange_y,Y_YellowOrange_before_filtered)):
			Diff_Y_YellowOrnge = iiii - eeee
			if Y_ArithmeticAverage_YellowOrange - Y_StandarDesv_YellowOrange < Diff_Y_YellowOrnge:
				Y_YellowOrange_Filtered.append(iiii)
		Y_YellowOrange_Filtered = list(OrderedDict.fromkeys(Y_YellowOrange_Filtered))
		#### counting the total of coordinates finally filtered
		number_X_YellowOrange = len(X_YellowOrange_Filtered)
		number_Y_YellowOrange = len(Y_YellowOrange_Filtered)
		HowManyYellowOrange = 0
		while HowManyYellowOrange < number_Y_YellowOrange-1 :
			HowManyYellowOrange = HowManyYellowOrange +1
			# print(HowManyYellowOrange, X_YellowOrange_Filtered)
			if number_X_YellowOrange != number_Y_YellowOrange and number_X_YellowOrange < number_Y_YellowOrange:
				X_YellowOrange_Filtered.append(xYellowOrang0)

		######		Joining the two x, y coordinates
		YellowOrange_filtered_coordenates = sorted(zip(Y_YellowOrange_Filtered, X_YellowOrange_Filtered ))
		#####	Print points as (x,y)
		# print(" Coordinate pairs for Green_filtered point ",Green_filtered_coordenates)
		###### 	Draw the rectangle in that case where it finds yellow orange
		for ptYellowOrange in YellowOrange_filtered_coordenates:
			####	cv2.rectangle(image where draw, place , color, thick line drawing)
			###		color BGR
			#Draw a rectangle around the adapted region found in this case
			cv2.rectangle(img, ptYellowOrange, (ptYellowOrange[0] + w_orange, ptYellowOrange[1] + h_orange), (0,255,255), 4)
			###	In this function the color goes BGR, what it does is put the text where it found the led
			cv2.putText(img, 'ORANGE', ptYellowOrange, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 4)
			##### 	Count the number of LEDs you found in this state
			Quantity_Leds_YellowOrange = Quantity_Leds_YellowOrange +1
		print("The number of LEDs in Yellow Orange state (on / problem) found is:      ", Quantity_Leds_YellowOrange)
				########## 						DARK ORANGE	COORDENATES FILTERS  									##########
	if len(location_dark_orange[0]) > 0:
		#####	For x on yellow orange before filtered
		for iterdarkorangX in sorted(location_dark_orange[0]):
			if iterdarkorangX not in OrangeOrange_x:
				OrangeOrange_x.append(iterdarkorangX)
		#### Compying the vector without repetitions to generate the second to compare
		X_OrangeOrange_before_filtered =  OrangeOrange_x.copy()
		####	Obtaining the first coordinate
		xOrangOrang0 = OrangeOrange_x[0]
		####	Deleting the first coordinate
		X_OrangeOrange_before_filtered.pop(0)
		#### 	The deleted coordinate is added to the result
		X_OrangeOrange_Filtered.append(xOrangOrang0)
		#####	orange orange same dark orange before filtering for y - basically vector obtained minus repeated coordinates
		for iterdarkorangY in sorted(location_dark_orange[1]):
			if iterdarkorangY not in OrangeOrange_y:
				OrangeOrange_y.append(iterdarkorangY)
		####	Compying the vector to generate the second
		Y_OrangeOrange_before_filtered =  OrangeOrange_y.copy()
		####	Gets the first coordinate obtained from the list of elements without repetitions
		yOrangOrang0 = OrangeOrange_y[0]
		###		Deleting the first element to be able to subtract with the complete list
		Y_OrangeOrange_before_filtered.pop(0)
		###		The deleted coordinate is added to the result
		Y_OrangeOrange_Filtered.append(yOrangOrang0)
		####	To automate the filtering, the dispersion measurements are calculated
		X_ArithmeticAverage_OrangOrang = ArithmeticAveragelist(OrangeOrange_x)
		# print("Arithmetic Average Orange Orange same as Dark Orange X", X_ArithmeticAverage_OrangOrang)
		X_Variance_OrangOrang = variance_list(OrangeOrange_x)
		# print("Variance Orange Orange same as Dark Orange X ", X_Variance_OrangOrang)
		X_StandarDesv_OrangOrang = StandarDesv(OrangeOrange_x)
		# print("Standard Desv same as Dark Orange X ", X_StandarDesv_OrangOrang)
		Y_ArithmeticAverage_OrangOrang = ArithmeticAveragelist(OrangeOrange_y)
		# print("rithmetic Average Orange Orange same as Dark Orange Y ", Y_ArithmeticAverage_OrangOrang)
		Y_Variance_OrangOrang = variance_list(OrangeOrange_y)
		# print("VVariance Orange Orange same as Dark Orange Y", Y_Variance_OrangOrang)
		Y_desvacion_estandar_NN = StandarDesv(OrangeOrange_y)
		# print(""Standard Desvr Orange Orange same as x Dark Orange Y ", Y_desvacion_estandar_NN)
		# print("Orange Orange same as x Dark Orange complete ",  OrangeOrange_x)
		# print("Orange Orange same as y Dark Orange complete", OrangeOrange_y)

		#### Applying the same method for filter similar X COORDENATES
		for nne,nni in sorted(zip(OrangeOrange_x,X_OrangeOrange_before_filtered)):
			Diff_X_OrangOrang = nni - nne
			# print("Diff Orange Orange ", Diff_X_OrangOrang, nni)
			if X_StandarDesv_OrangOrang<Diff_X_OrangOrang:
				X_OrangeOrange_Filtered.append(nni)
		X_OrangeOrange_Filtered = list(OrderedDict.fromkeys(X_OrangeOrange_Filtered))

		#### Applying the same method for filter similar Y COORDENATES
		for nnee,nnii in sorted(zip(OrangeOrange_y,Y_OrangeOrange_before_filtered)):
			Diff_Y_OrangOrang = nnii - nnee
			if Y_ArithmeticAverage_OrangOrang - Y_desvacion_estandar_NN < Diff_Y_OrangOrang:
				Y_OrangeOrange_Filtered.append(nnii)
		Y_OrangeOrange_Filtered = list(OrderedDict.fromkeys(Y_OrangeOrange_Filtered))
		##### Counting the total of coordinates finally filtered
		number_X_OrangOrang = len(X_OrangeOrange_Filtered)
		number_Y_OrangOrang = len(Y_OrangeOrange_Filtered)
		HowManyDarkOrange = 0
		while HowManyDarkOrange < number_Y_OrangOrang-1 :
			HowManyDarkOrange = HowManyDarkOrange +1
			# print(HowManyDarkOrange, X_OrangeOrange_Filtered)
			if number_X_OrangOrang != number_Y_OrangOrang and number_X_OrangOrang < number_Y_OrangOrang:
				X_OrangeOrange_Filtered.append(xOrangOrang0)

		######		Joining the two x, y coordinates
		OrangeOrange_filtered_coordenates = sorted(zip(Y_OrangeOrange_Filtered, X_OrangeOrange_Filtered))
		###### 	Draw the rectangle in that case where it finds orange orange
		for ptOrangOrang in OrangeOrange_filtered_coordenates:
			####	cv2.rectangle(image where draw, place , color, thick line drawing)
			###		color BGR
			#Draw a rectangle around the adapted region found in this case
			cv2.rectangle(img, ptOrangOrang, (ptOrangOrang[0] + w_dark_orange, ptOrangOrang[1] + h_dark_orange), (0,255,255), 4)
			###	In this function the color goes BGR, what it does is put the text where it found the led
			cv2.putText(img, 'DARK ORANGE', ptOrangOrang, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 4)
			##### 	Count the number of LEDs you found in this state
			Quantity_Leds_OrangeOrange = Quantity_Leds_OrangeOrange + 1
		print("The number of LEDs in Orange Orange status (problem / problem) found is:     ", Quantity_Leds_OrangeOrange)
	#### Shows me the figure already analyzed
	cv2.imshow("\nProcessed Image",img)
	### Since there are several, wait until you press a key and thus analyze the other image
	cv2.waitKey(0)
### Once finished remove all windows
cv2.destroyAllWindows()
