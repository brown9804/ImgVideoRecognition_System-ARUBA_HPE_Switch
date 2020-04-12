# Developer Guide

In order to run the program successfully, the following must be contained on your machine:

----------
OpenCV 4.1.2

Python 3.7.7

Numpy 1.15.2

The images used for the analysis are in .jpg format

----------



## Methods to characterize the image
An algorithm solves a particular problem, in this case the scenario of a laboratory is presented which, as indicated, does not present changes in the lighting and the captured images can contemplate a certain type of inclination as well as there may be modifications in the hardware since it is presented that you can analyze different switches. Once the initial tests have been carried out, these are the application of different filters with the intention of knowing the experimental characteristics of the images: Hue Saturation Value, filtering with upper and lower threshold (Limited color range), gray scale, scale to gray with threshold and binary cv2.THRESH_BINARY; it is observed that the behavior of the images with respect to the colors present in the original image and considering what the theory mentions tends to be an unexpected result.

## Identification methods
Following the aforementioned, different identification methods were tested, among which the following can be mentioned along with their result:



![image](https://github.com/brown9804/EIE_Project_stream_aruba_recognition/blob/master/Images_Recognition/ImgtoVerify/1GreenAngle.jpg)


**1. By contour** This method uses cv2.findContours and cv2.drawContours for which we obtain a result like the one shown in the image:




![image](https://drive.google.com/uc?export=view&id=15LgrQc-ybuNioDtGvtYb6XKHETdxiYPN)



**2. Contour adjusted with denoising:** If we try to improve the previous method, we opted to try to filter the image noise a little, for this a filter of cv2.fastNlMeansDenoisingColored was applied, for which we obtain the following:



![image](https://drive.google.com/uc?export=view&id=1bbmchlDV9M2E_l94OOukQelpTOyTjwEb)



**3. Using the contour method with two filters (fastNlMeansDenoisingColored):** If we visualize this test with the previous figure, we can see that it loses sharpness and therefore loses quality in the image.



![image](https://drive.google.com/uc?export=view&id=1ESZitSft19KaQPDkx_v59I3XO7LoJ3ou)




**4.Contour but capturing areas:** In this case, the image threshold was considered using cv2.threshold and cv2.findContours considering a minimum area found cv2.minAreaRec which returns a rotating rectangle and using cv2.boxPoints you can Access the pixels by traversing the points inside the box since it returns the coordinates of the corner points of the rotated rectangle.




![image](https://drive.google.com/uc?export=view&id=1i6NfTOcrCh7zdtAPKDgrrIYwLeGlmkwQ)



**5.Template method:**
##### Stage 1:

It did not work as expected, since the documentation recommended certain values in different parameters that did not allow adjusting the necessary recognition, so they were tested both experimentally and contemplating the tests carried out until optimal values were obtained for these images, as is the case. of the threshold. It should be remembered that this value is normalized between 0 and 1, so a value closer to one gives us greater precision.

##### Stage 2:
What this method does is to consider by pixel a part and the established threshold the values ​​that meet the conditions, obtaining in the same object identified for example LEDs in the ON state for the first port the following coordinates (145,1678), (146, 1678), (147,1679), (148,1677), (149,1677), (150,1676), (151,1677), (152,1677), (153,1678), (154,1675), (1515,1677), (156,1677) this being undesired therefore arithmetic calculations on a group of data were taken into account in this case the coordinates of the pixels to filter an object by location.


Finally, the algorithm present in the main.py was generated, capable of analyzing the different states of LEDs since, through the aforementioned tests, it is considered that the colors present in the image do not present abrupt changes except for possible light intensities which may be picked up when a port is on. In order to explain some decisions made and delve into the explanation in the main.py file, we proceed to contextualize different decisions.

* **Filtering noise / Making the image sharp:** Using Kittler's thresholding using the tool previously created at https://github.com/brown9804/Image_Segmentation_Project- a variance of 1: 15.39 is obtained, so values of 15 are used for the images since they are considered to be laboratory without changes in lighting. Taking into account the different tests, the values 15 15 7 15 (approximately 30s) are considered, despite the fact that the literature read recommends values of 10 10 7 21 (approximately 1:42 minutes). This is kept in the general code because it may be necessary to analyze images that due to the lack of sharpness the program does not work.

~~~~~~
# def denoising_sharpening(input):
#     sin_ruido= cv2.fastNlMeansDenoisingColored(input, None,15,15,7,15)
#     kernel=np.array([[-1,-1,-1,-1,-1],
#                       [-1,2,2,2,-1],
#                       [-1,2,8,2,-1],
#                       [-2,2,2,2,-1],
#                       [-1,-1,-1,-1,-1]])/8.0
#     sin_ruido = cv2.filter2D(sin_ruido,-1,kernel)
#     return sin_ruido


~~~~~~~~

* **Comparison operation using cv2.matchTemplate ():**
Template Matching is a method of searching and finding the location of a template image in a larger image. OpenCV comes with a cv2.matchTemplate () function for this purpose. Simply slide the template image over the input image (as in 2D convolution) and compare the template and the input image patch below the template image. Various comparison methods are implemented in OpenCV. Returns a grayscale image, where each pixel indicates how closely the neighborhood of that pixel matches the template. TM_CCOEFF_NORMED does Correlation coefficient, the method is simply used to:
a) make the template and image zero and
b) make the dark parts of the negative values of the image and the bright parts of the positive values of the image.

For example, inside the code you will find:

~~~~
res_verde = cv2.matchTemplate(img_gray,template_green,cv2.TM_CCOEFF_NORMED)
~~~~~

Whose parameters are: analyzed image converted to gray scale, image of the object you want to find, method to use.

* **Get the position where a pixel similar to the object was obtained:** This is done using np.where (), it returns elements where the implemented condition is met, in this case it returns a tuple with two arrays, one for the x coordinate and another one for the coordinate Y.

~~~~
###### gets the position of matching 
location_green = np.where(res_matching_green >= threshold)
location_orange = np.where(res_matching_orange >= threshold)
location_dark_orange = np.where(res_matching_dark_orange >= threshold)
~~~~

* **Encompassing the method used in the second stage mentioned in 5. Template method the following is followed:**
Sorted () is a method that returns a sorted list of the specified iterable object, so it is applied to the x coordinate.

~~~~~~
	for itergreenx in sorted(location_green[0]):
		if itergreenx not in Green_x:
			Green_x.append(itergreenx)
~~~~~~~

Since the intention of this method is to compare the difference between the previous coordinate, an array was generated that contains the same number of elements as the original array since the first coordinate is removed and the last one is copied, allowing the following logic to be performed of comparison put in example:
An arrangement is obtained with the coordinates (144, 145, 146, 147, 767, 768, 769, 771, 998, 1000, 1001) with the following code section a second arrangement is produced with the coordinates (145, 146, 147 , 767, 768, 769, 771, 998, 1000, 1001) so if we compare the first the element of the second arrangement with that of the second would give us the existing difference. This happens at the x coordinate.

~~~~
	###### Compying the vector without repetitions to generate the second to compare
	X_Green_before_filtered =  Geen_x.copy()
	######	Obtaining the first coordinate
	xGreen0 = Geen_x[0]
	###### Deleting the first coordinate
	X_Green_before_filtered.pop(0)
	######	The deleted coordinate is added to the result
	X_Green_Filtered.append(xGreen0)

~~~~~

It is applied to the coordinate Y, the same method of sorted ().

~~~~~
#####	Green before filtering for y - basically vector obtained minus repeated coordinates
	for itergreeny in sorted(location_green[1]):
		if itergreeny not in Green_y:
			Green_y.append(itergreeny)
~~~~~

As in the x coordinate, the same procedure is implemented for the coordinate and only in this case, values of
(1670,1671,1660,1670….) With very low differences between them, making sense since these differences are a product of the angle of inclination presented by the images.

~~~~~
	#####	Compying the vector to generate the second
	Y_Green_before_filtered =  Green_y.copy()
	##### Gets the first coordinate obtained from the list of elements without repetitions
	yGreen0 = Green_y[0]
	#######	Deleting the first element to be able to subtract with the complete list
	Y_Green_before_filtered.pop(0)
	######	The deleted coordinate is added to the result
	Y_Green_Filtered.append(yGreen0)
~~~~~

Considering the switch structure, matches are filtered since only one match per LED position is required, so this part of code shows where the difference is calculated and compares this difference between adjacent pixels with the value of the width and length of each template.

~~~~~~
##########   GREEN COORDENATES FILTERS ONE FOR LOCATION		##########
	#For green Y
	for e, i in sorted(zip(Green_y, Y_Green_before_filtered)):
		#Difference between y coordinates
		Diff_Y_Green = i - e
		if h_green < abs(Diff_Y_Green):
			Y_Green_Filtered.append(i)
	Y_Green_Filtered = list(OrderedDict.fromkeys(Y_Green_Filtered))
	# Filter for the X
	for ee, ii in sorted(zip(Green_x, X_Green_before_filtered)):
		#Difference between x coordinates
		Diff_X_Green = ii - ee
		if w_green < abs(Diff_X_Green):
			X_Green_Filtered.append(ii)
	X_Green_Filtered = list(OrderedDict.fromkeys(X_Green_Filtered))
~~~~~~~

Since very similar values are obtained for the Y coordinate, we count the number of filtered elements in the X coordinate arrangement and duplicate the first Y coordinate until the quantity of the X coordinate arrangement in elements equals. Finally obtaining the desired filtered coordinates.

~~~~~~
	#Counting the number of pixels each coordinate 
	number_X_Green = len(X_Green_Filtered)
	number_Y_Green = len(Y_Green_Filtered)
	HowManyGreen = 0
	#Equalizing in order the number of pixels Y
	while HowManyGreen < number_X_Green-1:
		HowManyGreen = HowManyGreen +1
		if number_Y_Green != number_X_Green and number_Y_Green < number_X_Green:
			Y_Green_Filtered.append(yGreen0)
	######		Joining the two x, y coordinates
	Green_filtered_coordenates = sorted(zip(X_Green_Filtered, Y_Green_Filtered))
~~~~~~


* **Drawing on the image at the same time allows counting the number of LEDs in a state:**

~~~~~~

###### 	Draw the rectangle and label in that case where it finds green
for ptGreen in Green_filtered_coordenates:
	####	cv2.rectangle(image where draw, place , color BGR, thick line drawing)
	cv2.rectangle(img, ptGreen, (ptGreen[0] + w_green, ptGreen[1] + h_green), (0,255,255), 4)
	###	In this function the color goes BGR, what it does is put the text where it found the led
	cv2.putText(img, 'GREEN', ptGreen, cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 255), 4)
	##### 	Count the number of LEDs you found in this state
	Quantity_Leds_Green = Quantity_Leds_Green +1
print("The number of LEDs in Green Green status (on / on) found is:      ", Quantity_Leds_Green)

~~~~~~

Where following the order in which the syntax of cv2.putTex () is found, it follows that the parameters correspond to the following: image where it will be drawn, text to add, recognized pixel of the template to identify, font, font scale , color (BGR), thickness of the line.

Resulting in:



![image](https://drive.google.com/uc?export=view&id=1dFEawbgMi-CZggnNFgdZQcxHB81sQ5yD)


