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

# result = np.zeros((height//2, width//2))
# for r in range(height):
#     if r%2==1:
#         continue
#     for c in range(width):
#         # print(crop_img[y, x])
#         if c%2==0:
#             result[r//2,c//2] = (green_img[r, c]/255)

# print(result)
def smaller_k_time(image, k):
    hr = height//k
    wr = width//k
    return size_change(image, hr, wr)

def size_change(image, hr, wr):
    height = len(image)
    width = len(image[0])
    result = np.zeros((hr, wr))
    if(height%hr == 0): kr = height//hr
    else: kr = height // hr + 1
    if(width%wr == 0): kc = width//wr
    else: kc = width//wr + 1
    r_dis, index_r = 0,-1

    for r in range(height):
        index_c = 0
        c_dis = 0
        if r % kr != 0 and r_dis < height - hr:
            r_dis += 1
            continue
        else: index_r += 1
        for c in range(width):
            if(c % kc == 0 or c_dis == width - wr):
                result[index_r, index_c] = (image[r, c]/255)
                index_c += 1
            else: c_dis += 1

    return result

image_resize = size_change(green_img, 250, 250)
# image_resize = smaller_k_time(green_img, 2)
cv2.imshow('Resize', image_resize)
cv2.waitKey(0)

# cv2.imshow('Result', result)
# cv2.imshow('Green', green_img)
# cv2.waitKey(0)

#image convolution
#2 function
