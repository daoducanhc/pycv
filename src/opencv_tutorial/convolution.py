import cv2
import numpy as np
img_path = 'resources/ex1.jpg'

img = cv2.imread(img_path)

height, width = img.shape[0], img.shape[1]

red_img = img[:, :, 2]

# cv2.imshow('Red', red_img)
# cv2.waitKey(0)

sobel = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

def convolve(img, kernel):
    img_height = img.shape[0]
    img_width = img.shape[1]

    kernel_height = len(kernel)
    kernel_width = len(kernel[0])

    result = np.zeros((img_height, img_width))

    H = (kernel_height - 1) // 2
    W = (kernel_width - 1) // 2

    for i in range(H, img_height - H):
        for j in range(W, img_width - W):
            sum = 0
            for y in range(-H, H+1):
                for x in range(-W, W+1):
                    a = img[i+y][j+x]
                    b = kernel[H+y][W+x]
                    sum += a*b
            result[i][j] = sum/255

    return result
result = convolve(red_img, translation)
cv2.imshow('Convolve', result)
cv2.waitKey(0)
