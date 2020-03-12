import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL,
 cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
clone = image.copy()

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(clone, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Bounding Boxes", clone)
cv2.waitKey(0)

# python src\opencv_tutorial\contour_to_futher\bounding_box.py --image resources/shapes.jpg
