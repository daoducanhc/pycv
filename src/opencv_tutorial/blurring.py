# cv2.blur
# cv2.gaussianblur
# cv2.medianblur
# cv2.bilateralfilter

import cv2
import numpy as np

img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)

blur = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img,(5,5),9)
median = cv2.medianBlur(img,5)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('Origin', img)
cv2.imshow('Blur', blur)
cv2.imshow('Gaussian', gaussian)
cv2.imshow('Median', median)
cv2.imshow('BilateralFilter', bilateralFilter)
cv2.waitKey(0)
