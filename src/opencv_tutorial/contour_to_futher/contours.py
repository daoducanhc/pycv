import argparse
import cv2
import numpy as np
import imutils

# img_path = 'resources/contours_ex.jpg'

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 255), 2)
print(len(cnts))

cv2.imshow('Original', image)
cv2.imshow('Contours', clone)
cv2.waitKey(0)

# python src/opencv_tutorial/contour_to_futher/contours.py --image resources/contours_ex.jpg
