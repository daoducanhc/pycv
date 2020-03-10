import cv2
import imutils

image = cv2.imread("resources/x_o.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for (i, c) in enumerate(cnts):
    area = cv2.contourArea(c)
    #find x, y to putText
    (x, y, w, h) = cv2.boundingRect(c)

    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area/hullArea
# o>0.98, x>0.6, ? = 0.279
    char = "?"

    if(solidity>0.98):
        char = "O"
    elif(solidity>0.6):
        char = "X"

    if(char != "?"):
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, char, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    print("{}: Contour #{} -- solidity = {:.2f}".format(char, i+1, solidity))

cv2.imshow("X_O", image)
cv2.waitKey(0)
