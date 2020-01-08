import cv2

img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)

# cv2.imshow('Image', img)
# cv2.waitKey(0)

height, width, channels = img.shape
print(f'{(height, width, channels)}')

b, g, r = img[5, 3] # row5 col3
print(f'{(b, g, r)}')

blue_img = img[:, :, 0]
green_img = img[:, :, 1]
red_img = img[:, :, 2]

# cv2.imshow('blue', blue_img)
# cv2.imshow('green', green_img)
# cv2.imshow('red', red_img)
# cv2.waitKey(0)

# img_resize = cv2.resize(img, (100, 100))
# cv2.imshow('Resize', img_resize)
# cv2.waitKey(0)

# crop_img = green_img[0:height, 0:10]
import numpy as np

result = np.zeros((height//2, width//2))
for r in range(height):
    if r%2==1:
        continue
    for c in range(width):
        # print(crop_img[y, x])
        if c%2==0:
            result[r//2,c//2] = (green_img[r, c]/255)

print(result)

cv2.imshow('Result', result)
cv2.imshow('Green', green_img)
cv2.waitKey(0)
