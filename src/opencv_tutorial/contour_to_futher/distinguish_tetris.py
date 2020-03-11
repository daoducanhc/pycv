import cv2
import imutils

image = cv2.imread("resources/tetris.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

clone = image.copy()
for (i, c) in enumerate(cnts):
    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)

    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area/hullArea
    aspectRatio = w / h
    print("Contour #{}: solidity = {:.2f} --- aspectRatio = {:.2f}".format(i+1, solidity, aspectRatio))

    shape = ""
    if(aspectRatio < 1.01): shape = "SQUARE"
    elif(aspectRatio > 3): shape = "RECTANGLE"
    elif(solidity >= 0.8 and aspectRatio < 1.49): shape = "Z-PIECE"
    elif(solidity < 0.8 and aspectRatio >= 1.49): shape = "L-PIECE"

    cv2.putText(clone, shape, (x+10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.drawContours(clone, [c], -1, (0,0,0), 2)
    cv2.imshow("Single", clone)
    cv2.waitKey(0)
