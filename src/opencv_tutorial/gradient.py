# func tinh 2 chieu gradient (2 anh) ngang = x (phai - trai), doc. = y (tren - duoi)
# 1 anh gradient orientation = arctan(Gy / Gx)

import cv2
import numpy as np

img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)
height, width, _ = img.shape
green_img = img[:, :, 1]

Gx = cv2.Sobel(green_img, ddepth = cv2.CV_64F, dx=1, dy=0)
Gy = cv2.Sobel(green_img, ddepth = cv2.CV_64F, dx=0, dy=1)
Gx = cv2.convertScaleAbs(Gx)
Gy = cv2.convertScaleAbs(Gy)
combine = cv2.addWeighted(Gx, 0.5, Gy, 0.5, 0)

cv2.imshow('Gx', Gx)
cv2.imshow('Gy', Gy)
cv2.imshow('Combine', combine)
cv2.waitKey(0)
