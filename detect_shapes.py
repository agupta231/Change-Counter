import imutils
import cv2
import numpy as np

image = cv2.imread("test_image.jpg")
resized = imutils.resize(image, width=500)

ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
blurred = cv2.bilateralFilter(gray, 15, 17, 17)

canny = cv2.Canny(blurred, 100, 200)
thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]

(cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)

    cv2.drawContours(resized, [c], -1, (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), 3)

    # if len(approx) > 5:
    #     cv2.drawContours(resized, [c], -1, (255, 0, 0), 4)

# cv2.drawContours(resized, cnts, -1, (0, 255, 0), 3)

cv2.imshow("bilat", blurred)
cv2.imshow("resized", resized)
cv2.imshow("canny", canny)
cv2.waitKey(0)