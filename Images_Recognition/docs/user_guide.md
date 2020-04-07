# User Guide

In order to run the program successfully, the following must be contained on your machine:

----------
OpenCV 4.1.2

Python 3.7.7

Numpy 1.15.2

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

Your computer will rename what comes before the $ in my case it is ~~~~~ Belindas-MacBook-Air: Images_Recognition belindabrown $ ~~~~~ , so it would look like this.

~~~~~
Belindas-MacBook-Air: Images_Recognition belindabrown $ python3 main.py
~~~~~

### Results

## Settings
