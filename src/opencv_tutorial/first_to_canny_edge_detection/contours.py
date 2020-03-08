import cv2
import numpy as np
import imutils

img_path = 'resources/contours_ex.jpg'

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = gray.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 255), 2)
print(len(cnts))

cv2.imshow('Contours', clone)
cv2.waitKey(0)
