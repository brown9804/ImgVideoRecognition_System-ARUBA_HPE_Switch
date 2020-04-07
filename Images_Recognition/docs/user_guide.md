# User Guide

In order to run the program successfully, the following must be contained on your machine:

----------
OpenCV 4.1.2

Python 3.7.7

Numpy 1.15.2

The images used for the analysis are in .jpg format

----------


## Functioning

### Run the program

**1. Change in absolute paths of templates**

Modify the absolute paths of the templates to use. This is found in the section of the main.py file which covers
shown below.

~~~~~
###### Read the template
template_green = cv2.imread ('', 0)
template_orange = cv2.imread ('', 0)
template_dark_orange = cv2.imread ('', 0)
~~~~~

You must enter the address corresponding to your machine in parentheses, for example:

/Users/belindabrown/Desktop/Folder1/Images_Recognition/Templates/ledOrange.jpg

**2. Change in location of images to verify**

The path where the folder containing the images you want to analyze must be modified. This part of the code is the corresponding block:

~~~~~
###### Directory with images verify
img_dir = ''
~~~~~

You must enter the address corresponding to your machine in parentheses, for example:

/ Users / belindabrown / Desktop / Folder1 / Images_Recognition / ImgtoVerify

**3. Algorithm execution**

In order for the Python interpreter to run the algorithm. You must go to the terminal or console that your machine owns, locate the file to be executed, which in this case is main.py, and put the following instruction

~~~~~
PathWhereIsMain.py USER $ python3 main.py
~~~~~

If we consider the example that has been used, it would be as follows:

Locating ourselves in the location / Users / belindabrown / Desktop / Folder1 / Images_Recognition

Your computer will rename what comes before the $ in my case it is: 
~~~~~ 
Belindas-MacBook-Air: Images_Recognition belindabrown $ 
~~~~~ 
So it would look like this.

~~~~~
Belindas-MacBook-Air: Images_Recognition belindabrown $ python3 main.py
~~~~~

### Results

It is necessary to contemplate that given the way in which the problem was posed, the analyzed image and its qualitative characteristics are displayed in IDLE, also, in the terminal the quantitative description of its properties is shown.


**1. Terminal Results**

Depending on what the image contains, different results will be obtained, which present a format like the following after following the **3. Algorithm execution** instruction:

~~~~~
/Users/belindabrown/Desktop/Folder1/Images_Recognition/ImgtoVerify/2OrangeOrange.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Orange Orange status (problem / problem) found is: 2 

/Users/belindabrown/Desktop/Folder1/Images_Recognition/ImgtoVerify/1YellowOrange.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Yellow Orange state (on / problem) found is: 1 

/Users/belindabrown/Desktop/Folder1/Images_Recognition/ImgtoVerify/5Green.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Green Green status (on / on) found is: 5 

/Users/belindabrown/Desktop/Folder1/Images_Recognition/ImgtoVerify/1Mixed.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Green Green status (on / on) found is: 1
The number of LEDs in Yellow Orange state (on / problem) found is: 1
The number of LEDs in Orange Orange status (problem / problem) found is: 1 

~~~~~

**2. Shown in Python IDLE**

A few seconds later it is shown depending on the cases and the number of LEDs that are lit, a window will be displayed with an analyzed image, to analyze the next image press any key.

**Note:** If a zoomed image is displayed, consider double-clicking on the top bar of the window in order for the image to readjust.

## Settings
If we consider the development algorithm, at the recognition level several changes can be made:

**1. Change of the object or objects to recognize**

    **1.1 Template is modified**  Once it has been decided which objects are going to be identified, these images are stored in an exclusive folder for templates, these images throughout the code are called as templates.
    
    **1.2 Modify images to verify** If you want to change what is identified in the images, it is recommended to store all the images in a folder first. Following the recognition model present in this section.
    
    **1.3 Quantity of objects**
The number of objects it identifies are 3 (different states), but if you want to increase or decrease the number of items, the idea would be to eliminate or add, whatever the case may be, a complete block contemplating the instructions provided. That is, you can guide yourself by looking at what elements the GREE object contains and thus identifying what belongs to it.

~~~~~
######## FOR GREEN ######
###### COMPARING X
Geen_x = []
X_Green_before_filtered = []
###### COMPARING Y
Green_y = []
Y_Green_before_filtered = []
###### THE FILTERED GREEN COORDINATES
X_Green_Filtered = []
Y_Green_Filtered = []
######## TO JOIN THE TWO GREEN VECTORS
Green_filtered_co ordinate = []
###### Number of LEDs in state # XXX
Quantity_Leds_Green = 0
~~~~~


~~~~~
######## COMPARING THE IMAGE USING TEMPLATE METHOD ########
res_matching_green = cv2.matchTemplate (img_gray, template_green, cv2.TM_CCOEFF_NORMED)
~~~~~

~~~~
###### Gets the position
	location_green = np.where(res_matching_green >= threshold)
~~~~~


```		########## IF THERE IS GREEN THEN ... ##########
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
	########## 		GREEN	COORDENATES FILTERS  	##########
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
```
2. Threshold adjustment: Run the program and check if it identifies well, if not adjust the threshold. It is currently at 0.92 remembering that its value is in a range between 0 - 1, the closer it is to the more accurate it is.

~~~
######	Specifying (threshold)
threshold= 0.92
~~~
