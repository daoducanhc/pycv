import cv2
import imutils

image = cv2.imread("resources/receipt.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 75, 200)

cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,
 cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:7]

for c in cnts:
    # cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01*peri, True)

    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
cv2.imshow("Receipt", image)
cv2.waitKey(0)
