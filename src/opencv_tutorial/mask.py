import cv2
import numpy as np

img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)
height, width, _ = img.shape
green_img = img[:, :, 1]

green_img = cv2.GaussianBlur(green_img, (7,7), 0)
# T, mask = cv2.threshold(green_img, 128, 255, cv2.THRESH_BINARY)
T, mask = cv2.threshold(green_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
adaptive = cv2.adaptiveThreshold(green_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 15)
result = cv2.bitwise_and(green_img, green_img, mask=mask)

print(T)
cv2.imshow('Adaptive', adaptive)
cv2.imshow('Mask', mask)
cv2.imshow('Threshold', result)
cv2.waitKey(0)
