import cv2
import numpy as np

img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)
height, width, _ = img.shape
green_img = img[:, :, 1]

structuring_element = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

def dilation(img, se):
    img_height = img.shape[0]
    img_width = img.shape[1]
    se_height = len(se)
    se_width = len(se[0])

    result = np.zeros((img_height, img_width))

    H = (se_height - 1) // 2
    W = (se_width - 1) // 2

    for i in range(img_height):
        for j in range(img_width):
            max = 0
            for y in range(-H, H+1):
                for x in range(-W, W+1):
                    a = i+y
                    b = j+x
                    if(a<0 or b<0 or a>img_height-1 or b>img_width-1): k = 0
                    else: k = img[a][b]

                    if(max < k*se[H+y][W+x]):
                        max = k*se[H+y][W+x]
            result[i][j] = max/255

    return result

def erosion(img, se):
    img_height = img.shape[0]
    img_width = img.shape[1]
    se_height = len(se)
    se_width = len(se[0])

    result = np.zeros((img_height, img_width))

    H = (se_height - 1) // 2
    W = (se_width - 1) // 2

    for i in range(img_height):
        for j in range(img_width):
            min = 255
            for y in range(-H, H+1):
                for x in range(-W, W+1):
                    if(se[H+y][W+x] == 0): continue
                    a = i+y
                    b = j+x
                    if(a<0 or b<0 or a>img_height-1 or b>img_width-1):
                        k = 0
                    else: k = img[a][b]

                    if(min > k*se[H+y][W+x]):
                        min = k*se[H+y][W+x]
            result[i][j] = min/255

    return result

def opening(img, se):
    img_height = img.shape[0]
    img_width = img.shape[1]
    temp = np.zeros((img_height, img_width))
    result = np.zeros((img_height, img_width))

    temp = erosion(img, se)
    result = dilation(temp*255, se)
    return result

def closing(img, se):
    img_height = img.shape[0]
    img_width = img.shape[1]
    temp = np.zeros((img_height, img_width))
    result = np.zeros((img_height, img_width))

    temp = dilation(img, se)
    result = erosion(temp*255, se)
    return result

dilated = dilation(green_img, structuring_element)
eroded = erosion(green_img, structuring_element)
opened = opening(green_img, structuring_element)
closed = closing(green_img, structuring_element)
print(dilated[0][0]*255)
print(green_img[0][0])
cv2.imshow('Origin', green_img)
cv2.imshow('Dilated', dilated)
cv2.imshow('Erosted', eroded)
cv2.imshow('Opened', opened)
cv2.imshow('Closed', closed)

cv2.waitKey(0)
