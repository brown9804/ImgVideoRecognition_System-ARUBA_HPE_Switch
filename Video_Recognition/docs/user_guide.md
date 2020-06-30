# User Guide

In order to run the program successfully, the following must be contained on your machine:

----------
OpenCV 4.1.2

Python 3.7.7

Numpy 1.15.2

The images used for the analysis are in .jpg format

----------


## Functioning

This algorithm is divided into two sections:
* The first section consists of dividing the video into frames per second according to what is requested by the user. That is, the user inserts how often they want to capture an image of the complete video.
* The second section is the analysis that was implemented for the image analysis operation mode which is found in the "Images_Recognition" folder.

### Run the program
#Important: Make the changes that are mentioned in the two sections changes.

In order to facilitate the development of the program, a makefile was implemented which follows the following instructions:

1. To split the video into frames per second you must enter the console being in a path like the following:
<Where the folders / Video_Recognition are stored> $ make frames

2. To recognize the state of the ports, the following is followed:
<Where folders / Video_Recognition are stored> $ make analize

### Changes in frame_videos.py

**1. Change the absolute paths of the video that will be analize**

~~~~~
######	Directory with images verify
img_dir = ''

Example:
/Users/belindabrown/Desktop/EIE_Project_stream_aruba_recognition-master/Video_Recognition/VdstoVerify/

img_dir = '/Users/belindabrown/Desktop/EIE_Project_stream_aruba_recognition-master/Video_Recognition/VdstoVerify/'
~~~~~

**2. Change the absolute path of the frames result**


~~~~~
cv2.imwrite('/%s.jpg'%for_name, img) #Need path

Example:
/Users/belindabrown/Desktop/EIE_Project_stream_aruba_recognition-master/Video_Recognition/FramestoVerify

cv2.imwrite(/Users/belindabrown/Desktop/EIE_Project_stream_aruba_recognition-master/Video_Recognition/FramestoVerify/%s.jpg'%for_name, img) #Need path
~~~~~


### Changes in main.py

Before using the makefile instructions, you must make the pertinent changes regarding the addresses where the information you are going to work with is located.



**1. Change in absolute paths of templates**

Modify the absolute paths of the templates to use. This is located in the section of the main.py file where a part of the algorithm similar to what is shown below is found.

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

/Users/belindabrown/Desktop/Folder1/Images_Recognition/ImgtoVerify

**3. Algorithm execution**

In order for the Python interpreter to run the algorithm. You must go to the terminal or console that your machine owns, locate the file to be executed, which in this case is main.py, and put the following instruction.

~~~~~
<PathWhereIsMain.py USER>$ python3 main.py
~~~~~

If we consider the example that has been used, it would be as follows:

Locating ourselves in:

/Users/belindabrown/Desktop/Folder1/Images_Recognition

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


It is necessary to contemplate that given the way in which the problem was posed, the analyzed image and its qualitative characteristics are displayed in IDLE, also, in the terminal the quantitative description of its properties is shown.


**1. Terminal Results**

Depending on what the image contains, different results will be obtained that are presented in a format like the following. This happens after applying what is described in the section **3. Algorithm execution**:

~~~~~
 /Users/belindabrown/Desktop/EIE_Project_stream_aruba_recognition-master/Images_Recognition/ImgtoVerify/3YellowOrange.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Yellow Orange state (on / problem) found is:       3
The number of ports are:       12
Positions of the leds ON found [149, 814, 2124]
Port 1 statuts:						Orange
Port 3 statuts:						Orange
Port 7 statuts:						Orange

 /Users/belindabrown/Desktop/EIE_Project_stream_aruba_recognition-master/Images_Recognition/ImgtoVerify/1Mixed.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Green Green status (on / on) found is:       1
The number of LEDs in Yellow Orange state (on / problem) found is:       1
The number of LEDs in Orange Orange status (problem / problem) found is:      1
The number of ports are:       12
Positions of the leds ON found [140, 800, 1446]
Port 1 statuts:						Green
Port 3 statuts:						Orange
Port 5 statuts:						Dark Orange

 /Users/belindabrown/Desktop/EIE_Project_stream_aruba_recognition-master/Images_Recognition/ImgtoVerify/4YellowOrange.jpg
Image loaded, analyzing patterns ...
The number of LEDs in Yellow Orange state (on / problem) found is:       4
The number of ports are:       12
Positions of the leds ON found [149, 814, 2124, 3434]
Port 1 statuts:						Orange
Port 3 statuts:						Orange
Port 7 statuts:						Orange
Port 11 statuts:					Orange
~~~~~
**2. Shown in Python IDLE**

A few seconds later it is shown depending on the cases and the amount of LEDs that are lit, a window with a analyzed image will be displayed and to continue with the next image press any key.

**Note:** If a zoomed image is displayed, consider double-clicking on the top bar of the window in order for the image to readjust.

## Settings
If we consider the algorithm developed at the recognition level, several changes can be made:

**1. Change of the object or objects to recognize:**

    **1.1 Template is modified:**  Once it has been decided which objects are going to be identified, these images are stored in an exclusive folder for templates, these images throughout the code are called as templates.
    
    **1.2 Modify images to verify:** If you want to change what is identified in the images, it is recommended to store all the images in a folder first. Following the recognition model present in this section.
    
    **1.3 Quantity of objects:** The number of objects it identifies are 3 (different states), but if you want to increase or decrease the number of items, the idea would be to eliminate or add, whatever the case may be, call the function again but enter the corresponding parameters.

~~~~~
res_matching_green = cv2.matchTemplate(<image in gray>,<template that is going to used>,cv2.TM_CCOEFF_NORMED)

Example:
res_matching_green = cv2.matchTemplate(img_gray,template_green,cv2.TM_CCOEFF_NORMED)
~~~~~

Add this line following the parameters:

~~~~~
location_green = np.where(res_matching_green >= threshold)
~~~~~

Call the fucntion like this example:

~~~~~
X_Green_Filtered0 = color_filter(location_green, w_green, h_green, img, 'GREEN')
~~~~~

Check if the array is empty at:

~~~~~
# Checking empty
if X_Green_Filtered0:
	X_Green_Filtered = list(OrderedDict.fromkeys(X_Green_Filtered0))
else:
	X_Green_Filtered = []
~~~~~

Pixels are added in the ordered list to recognize the positions of the ports and match them to the LEDs to get the status of each port.
~~~~~
leds_on_fnd = sorted(list(OrderedDict.fromkeys(X_YellowOrange_Filtered + X_Green_Filtered + X_OrangeOrange_Filtered)))
~~~~~

Finally, another elif must be implemented like the one in the following example:

~~~~~
elif j in X_OrangeOrange_Filtered:
	print("Port", i[1], "status:	
~~~~~

**2. Threshold adjustment:** Run the program and check if it identifies well, if not adjust the threshold. It is currently at 0.90 remembering that its value is in a range between 0 - 1, the closer it is to the more accurate it is.

~~~
######	Specifying (threshold)
threshold= 0.90
thresholdport= 0.70
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

**4. Messages on screen:** It prints the results of 3 sections of the process, name of the image analyzed, an announcement that the image has been loaded, this shows us that the process of acquiring the data of said image was successful and finally prints the result of how many LEDs are in each state, being these:

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
