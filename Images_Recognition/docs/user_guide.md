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
