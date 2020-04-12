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

/Users/belindabrown/Desktop/Folder1/Images_Recognition/ImgtoVerify/4Mixed.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Green Green status (on / on) found is:       4
The number of LEDs in Yellow Orange state (on / problem) found is:       4
The number of LEDs in Orange Orange status (problem / problem) found is:      4


~~~~~

**2. Shown in Python IDLE**

A few seconds later it is shown depending on the cases and the number of LEDs that are lit, a window will be displayed with an analyzed image, to analyze the next image press any key.

**Note:** If a zoomed image is displayed, consider double-clicking on the top bar of the window in order for the image to readjust.

## Settings
If we consider the development algorithm, at the recognition level several changes can be made:

**1. Change of the object or objects to recognize:**

    **1.1 Template is modified:**  Once it has been decided which objects are going to be identified, these images are stored in an exclusive folder for templates, these images throughout the code are called as templates.
    
    **1.2 Modify images to verify:** If you want to change what is identified in the images, it is recommended to store all the images in a folder first. Following the recognition model present in this section.
    
    **1.3 Quantity of objects:** The number of objects it identifies are 3 (different states), but if you want to increase or decrease the number of items, the idea would be to eliminate or add, whatever the case may be, a complete block contemplating the instructions provided. That is, you can guide yourself by looking at what elements the GREE object contains and thus identifying what belongs to it.

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

	########## 		GREEN	COORDENATES FILTERS ONE FOR LOCATION 	##########
	#For green X
	for e, i in sorted(zip(Geen_x, X_Green_before_filtered)):
		#Difference between x coordinates
		Diff_X_Green = i - e
		if h_green < abs(Diff_X_Green):
			X_Green_Filtered.append(i)
	X_Green_Filtered = list(OrderedDict.fromkeys(X_Green_Filtered))
	# Filter green y
	for ee, ii in sorted(zip(Green_y, Y_Green_before_filtered)):
		#Difference between y coordinates
		Diff_Y_Green = ii - ee
		if w_green < abs(Diff_Y_Green):
			Y_Green_Filtered.append(ii)
	Y_Green_Filtered = list(OrderedDict.fromkeys(Y_Green_Filtered))
	#Counting the number of pixels each coordinate 
	number_X_Green = len(X_Green_Filtered)
	number_Y_Green = len(Y_Green_Filtered)
	HowManyGreen = 0
	#Equalizing in order the number of pixels Y
	while HowManyGreen < number_Y_Green-1:
		HowManyGreen = HowManyGreen +1
		# print(HowManyGreen, X_Green_Filtered)
		if number_X_Green != number_Y_Green and number_X_Green < number_Y_Green:
			X_Green_Filtered.append(xGreen0)
	# print("X_Green_Filtered", X_Green_Filtered)
	# print("Y_Green_Filtered", Y_Green_Filtered)
	######		Joining the two x, y coordinates
	Green_filtered_coordenates = sorted(zip(Y_Green_Filtered, X_Green_Filtered))
	###### 	Draw the rectangle and label in that case where it finds green
	for ptGreen in Green_filtered_coordenates:
		####	cv2.rectangle(image where draw, place , color BGR, thick line drawing)
		cv2.rectangle(img, ptGreen, (ptGreen[0] + w_green, ptGreen[1] + h_green), (0,255,255), 4)
		###	In this function the color goes BGR, what it does is put the text where it found the led
		cv2.putText(img, 'GREEN', ptGreen, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 4)
		##### 	Count the number of LEDs you found in this state
		Quantity_Leds_Green = Quantity_Leds_Green +1
	print("The number of LEDs in Green Green status (on / on) found is:      ", Quantity_Leds_Green)
```
**2. Threshold adjustment:** Run the program and check if it identifies well, if not adjust the threshold. It is currently at 0.90 remembering that its value is in a range between 0 - 1, the closer it is to the more accurate it is.

~~~
######	Specifying (threshold)
threshold= 0.90
~~~

**3. Modifications to the image**

**3.1. Text (recognized object tags):** can modify the format of the text which is added in the image, for the previous cases we have GREEN, YELLOW ORANGE, ORANGE, these labels that are added on the image have a format of color, letter, and line thickness.
	
~~~
###	In this function the color goes BGR, what it does is put the text where it found the led
	cv2.putText(img, 'GREEN', ptGreen, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 4)
~~~

Where following the order in which the syntax of `cv2.putTex ()` is found, it follows that the parameters correspond to the following: `image where it will be drawn, text to add, recognized pixel of the template to identify, font, font scale, color (BGR), thickness of the line`.

**3.2. Rounding format:** In this case, given the shape of the objects to be recognized, it was decided to implement a rectangular contour. For the above reason, `cv2.rectangle` is used, although if you want it to be circular, it is recommended to search the OpenCV documentation for `cv2.circle`.

~~~
####	cv2.rectangle(image where draw, place , color BGR, thick line drawing)
cv2.rectangle(img, ptGreen, (ptGreen[0] + w_green, ptGreen[1] + h_green), (0,255,255), 4)
~~~

**4. Messages on screen:** Print the results of 3 sections of the process, name of the image analyzed, an announcement that the image has been loaded, this shows us that the process of acquiring the data of said image was successful and finally prints the result of how many LEDs are in each state, being these:

***First section***

~~~
	print("\n", f1) #picture name
~~~

***Second section***

~~~
	###### Announces every time an image is reviewed
	print("Image loaded, analyzing patterns ...")
~~~

***Third section***

~~~
	print("The number of LEDs in Green Green status (on / on) found is:      ", Quantity_Leds_Green)
	print("The number of LEDs in Yellow Orange state (on / problem) found is:      ", Quantity_Leds_YellowOrange)
	print("The number of LEDs in Orange Orange status (problem / problem) found is:     ", Quantity_Leds_OrangeOrange)
~~~
