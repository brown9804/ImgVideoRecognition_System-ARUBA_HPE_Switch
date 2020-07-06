# Developer Guide

----------

University of Costa Rica

Belinda Brown, timna.brown@ucr.ac.cr

June, 2020

----------


In order to run the program successfully, the following must be contained on your machine:

----------
OpenCV 4.1.2

Python 3.7.7

Numpy 1.15.2

The images used for the analysis are in .jpg format

----------



## Methods to characterize the image
An algorithm solves a particular problem, in this case the scenario of a laboratory is presented that (as indicated) does not present changes in lighting and the captured images can contemplate a certain type of inclination, as well as there may be modifications in the hardware that It is presented that you can analyze different switches. Although once the initial tests have been carried out, the behavior of the images with respect to the colors present in the original image is observed and what the theory mentions to an unexpected result is considered. These tests can be summarized in the application of different filters with the intention of knowing the experimental characteristics of the images: hue saturation value, filter with upper and lower threshold (limited color range), gray scale, scale to gray with threshold and binary "cv2.THRESH_BINARY".

## Identification methods
Following the above, different identification methods were tested, among which the following can be mentioned along with their result:



![image](https://github.com/brown9804/EIE_Project_stream_aruba_recognition/blob/master/Images_Recognition/ImgtoVerify/1GreenAngle.jpg)


**1. By contour** This method uses cv2.findContours and cv2.drawContours for which we get a result like the one shown in the image:


![image](https://drive.google.com/uc?export=view&id=15LgrQc-ybuNioDtGvtYb6XKHETdxiYPN)



**2. Contour adjusted with denoising:** If it's try to improve the previous method, you choose to slightly filter the image noise, for this a filter of cv2.fastNlMeansDenoisingColored was applied, where you get:


![image](https://drive.google.com/uc?export=view&id=1bbmchlDV9M2E_l94OOukQelpTOyTjwEb)



**3. Using the contour method with two filters (fastNlMeansDenoisingColored):** When this test is displayed, it is compared with this result and with the result of the method contour adjusted with noise elimination titulo_controno_no_noise, it is appreciated that sharpness is lost at the same time that image quality is lost.

![image](https://drive.google.com/uc?export=view&id=1ESZitSft19KaQPDkx_v59I3XO7LoJ3ou)




**4.Outlined but capturing areas:** In this case, certain considerations were made: 
 
* The image threshold using cv2.threshold and cv2.findContours.
 
* A minimal area using cv2.minAreaRec that returns a rotating rectangle and through cv2.boxPoints you can access the pixels that form inside the rectangle since it returns The coordinates of the corner points of the rotated rectangle.




![image](https://drive.google.com/uc?export=view&id=1i6NfTOcrCh7zdtAPKDgrrIYwLeGlmkwQ)



**5.Template method:**
It did not work as expected, since the documentation recommended certain values in different parameters that did not allow adjusting the necessary recognition, therefore the parameters were tested both experimentally and by the history of the previous methods. Ending with obtaining the optimal values for these images, such as the threshold value.

Remember that the value of this threshold must be a normalized value, that is, between 0 and 1 where a value closer to one gives us greater precision.

##### Stage 2:
What this method does is to consider each pixel and the established threshold the values ​​that the conditions consider. The result is a large number of pixels that match the identification of the LED template in a certain state. For example, applying this method on the image \ ref {fig:
base_historial_imagen} we determine as base of explanation, for the first LED which can be seen that the ordered pairs of the location of the state ON for the first port: (145,1678), (146, 1678), (147,1679), (148,1677), (149,1677), (150,1676), (151,1677), (152,1677), (153,1678), (154, 1675), (1515,1677), (156 , 1677) this is not desired, therefore, several arithmetic calculations were considered in order to be able to filter the coordinates obtained only by location.


Finally, the algorithm present in main.py was generated, capable of analyzing the different states of the LED development from the study and implementation, whether positive results or inconclusive tests that will provide knowledge about the characteristics of the recognition of the desired objects. Consider that the colors present in the image do not show abrupt changes, except for the possible light intensities that can be recovered when a port is activated.


To explain some decisions made and delve into the explanation in the main.py file, we continue with the contextualization of different decisions.

* **Filtering noise / Making the image sharp:** Using Kittler's thresholding using the tool previously created at https://github.com/brown9804/Image_Segmentation_Project- a variance of 1: 15.39 is obtained, so values of 15 are used for the images since they are considered to be laboratory without changes in lighting. Taking into account the different tests, the values 15 15 7 15 (approximately 30s) are considered, despite the fact that the literature read recommends values of 10 10 7 21 (approximately 1:42 minutes). This is kept in the general code because it may be necessary to analyze images that due to the lack of sharpness the program does not work completelly weel.

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
Template matching (cv2.matchTemplate) is a method of searching and finding the location of a template image in a larger image. OpenCV comes with a cv2.matchTemplate () function for this purpose. It works by sliding the template image over the input image (as in 2D convolution), comparing the template and the input image patch below the template image. By combining various OpenCV comparison methods, get a grayscale image, where each pixel indicates how closely they match that pixel's neighborhood to the template. TM_CCOEFF_NORMED does the correlation coefficient, the method is simply used to:

a) Make the template and image zero.

b) Make the dark parts of the negative values of the image and the bright parts of the positive values of the image.

For example, within the found code:

~~~~
res_matching_green = cv2.matchTemplate(<image in gray>,<template that is going to used>,cv2.TM_CCOEFF_NORMED)

Example:
res_matching_green = cv2.matchTemplate(img_gray,template_green,cv2.TM_CCOEFF_NORMED)
~~~~~

Whose parameters are: analyzed image converted to gray scale, image of the object you want to find, method to use.

* **Get the position where a pixel similar to the object was obtained:** This is done using np.where (), it returns the elements where the implemented condition is met, in this case it returns a tuple with two matrices one for the coordinate x and another for the Y coordinate.

~~~~
location = np.where(<res of matching template>    >=  <It is a threshold constant which is set according to the light variations that are possessed>

Example:
location_green = np.where(res_matching_green >= threshold)
~~~~

* **Order the pixels obtained to relate them to the positions of the LEDs of each port:**
Sorted () is a method that returns an ordered list of the specified iterable object, so it is applied to the x coordinate.

~~~~~~
for itergreenx in sorted(location_green[0]):
	if itergreenx not in Green_x:
		Green_x.append(itergreenx)
~~~~~~~

Since the intention of this method is to compare the difference between the previous coordinate, an array containing the same number of elements as the original array is generated, the first coordinate is removed and the last coordinate is copied, allowing the following logic to which will be exemplified by taking the initial image as the basis for analysis.

An array is obtained with the coordinates (144, 145, 146, 147, 767, 768, 769, 771, 998, 1000, 1001) with the following code section, a second array is produced with the coordinates (145, 146, 147, 767, 768, 769, 771, 998, 1000, 1001) so if you compare the first value of the array, the element of the second array with the second would give us the existing difference.

This happens at the x coordinate:

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

As in the x coordinate, the same procedure is implemented for the coordinate and only in this case, values of (1670,1671,1660,1670….) With very low differences between them, making sense since these differences are a product of angle of angular inclination in the taking of images.

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

Taking into account the structure of the algorithm, it is already able to filter the matches (the reason why filtering is required is that there should only be one pixel per LED position. This part of the code shows where the difference is calculated and compares this difference between pixels. adjacent with the value of the width and length of each template.

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

Since very similar values are specified for the Y coordinate, we count the number of elements filtered in the X coordinate array and double the first Y coordinate until the number of marine elements is equal to the size of the Y coordinate array and the coordinates X be the same. 

Finally, the filtered coordinates are obtained, this being what is desired.
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

In order to explain the parameters of cv2.putTex (), follow the parameters corresponding to the following: image where it will be drawn, text to add, recognized pixel of the template to identify, font, font scale, color (BGR), line thickness.


* **Change the x-axis recognition range:**
This stage (is the one shown below) is used to relate the position of the ports, where a template of two ports is taken and to obtain their total quantity it is multiplied by two. Since the template is identified starting at position x0, the upper left corner is considered an adjustable range for this relationship.

~~~~
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
				print("Port", i[1], "status:
~~~~
To adjust the parameters, the values ​​are modified in:
~~~~
if x in range(-150,70):
~~~~
It is recommended to modify the first value being this -150 decreasing this value towards -∞.
 
Resulting in:



![image](https://drive.google.com/uc?export=view&id=1iTSRdDFFLdisww2V66w8bsXMxrH6s99g)


