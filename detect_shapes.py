import imutils
import cv2
import numpy as np

image = cv2.imread("test_image.jpg")
resized = imutils.resize(image, width=300)

ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

canny = cv2.Canny(resized, 100, 200)
thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]

(cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(resized, cnts, -1, (0, 255, 0), 3)

cv2.imshow("resized", resized)
cv2.waitKey(0)