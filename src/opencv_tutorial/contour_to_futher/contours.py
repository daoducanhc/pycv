import argparse
import cv2
import numpy as np
import imutils

# img_path = 'resources/contours_ex.jpg'

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_LIST for inside <-> cv2.RETR_EXTERNAL just for outside
cnts = imutils.grab_contours(cnts)
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print(len(cnts))

cv2.imshow('Original', image)
cv2.imshow('Contours', clone)
cv2.waitKey(0)

# python src/opencv_tutorial/contour_to_futher/contours.py --image resources/contours_ex.jpg

clone = image.copy()
cv2.destroyAllWindows()

for(i,c) in enumerate(cnts):
    print("Drawing contour #{}".format(i+1))
    cv2.drawContours(clone, [c], -1, (0, 0, 255), 2)
    cv2.imshow("Single contour", clone)
    cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()

for c in cnts:
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)

    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
    cv2.waitKey(0)
