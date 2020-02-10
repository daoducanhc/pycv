import cv2
# import numpy as np

img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)

edged = cv2.Canny(img, 100, 200)

cv2.imshow('Origin', img)
cv2.imshow('Canny detected', edged)
cv2.waitKey(0)
