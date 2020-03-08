import cv2
import numpy as np

img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)
height, width, _ = img.shape
green_img = img[:, :, 1]

# translation = np.float32([[1, 0, 25], [0, 1, 50]])
# shifted = cv2.warpAffine(green_img, translation, (width, height))

# rotation = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
# shifted = cv2.warpAffine(green_img, rotation, (width, height))
# cv2.imshow('Image', shifted)

# r = 600 / width
# h = int(r*height)
# resized = cv2.resize(green_img, (600, h), interpolation=cv2.INTER_LANCZOS4)
# cv2.imshow('Image', resized)

# flipped0 = cv2.flip(green_img, 0)
# flipped1 = cv2.flip(green_img, 1)
# cv2.imshow('Image0', flipped0)
# cv2.imshow('Image1', flipped1)

# cropped = green_img[100:300, 100:200]
# cv2.imshow('Image', cropped)

# m = np.ones((height, width), dtype='uint8') * 20
# added = cv2.add(green_img, m)
# subtracted = cv2.subtract(green_img, m)
# cv2.imshow('Image', subtracted)
# cv2.imshow('Image1', added)

# circle = np.zeros((height, width), dtype='uint8')
# cv2.circle(circle, (width//2, height//2), 50, 100, -1)
# and_ = cv2.bitwise_and(green_img, circle)
# or_ = cv2.bitwise_or(green_img, circle)
# xor_ = cv2.bitwise_xor(green_img, circle)
# not_ = cv2.bitwise_not(green_img)
# cv2.imshow('Image', not_)

# m = np.zeros(img.shape[:2], dtype='uint8')
# cv2.circle(m, (width//2, height//2), 70, 100, -1)
# masked = cv2.bitwise_and(green_img, green_img, mask=m)
# cv2.imshow('Image', masked)

B, G, R = cv2.split(img)
m = np.zeros((height, width), dtype='uint8')
merged1 = cv2.merge([B, m, m])
merged2 = cv2.merge([m, G, m])
merged3 = cv2.merge([m, m, R])

cv2.imshow('Blue', merged1)
cv2.imshow('Green', merged2)
cv2.imshow('Red', merged3)


cv2.waitKey(0)
#morphological operations 4 func
