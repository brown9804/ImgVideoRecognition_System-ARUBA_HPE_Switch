#Python3

#                   For Video_Recognition


# Making python makefile because we need to
# delete the result photos
###
######## belindabrownr@gmail.com
###

#******************************************************************************
############  		Modify this part with your own
############ 			files/folders paths.
#******************************************************************************
# Frames result folder
FR = ./FramestoVerify/
SRC = ./src/




#******************************************************************************
############ 						Run python script
#******************************************************************************
all: frames analyze

frames:
	python3 $(SRC)frame_videos.py

analyze:
	python3 $(SRC)main.py

#******************************************************************************
############ 							CLEAN FOR ALL
#******************************************************************************


.PHONY: clean
clean:
	rm -rf $(FR)*.jpg
