import cv2
import imutils
import numpy

image_raw = cv2.imread("test_image_2.jpg")
resized = imutils.resize(image_raw, width=400)

hsv_image = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)

cv2.imshow("hue", h)
cv2.imshow("saturation", s)
cv2.imshow("value", v)

s_bilat = cv2.bilateralFilter(s, 15, 17, 17)

edged = cv2.Canny(s_bilat, 100, 200)
cv2.imshow("edged", edged)

dilation = cv2.dilate(edged, numpy.ones((5, 5), numpy.uint8), iterations=1)

print len(cv2.findContours(dilation.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE))
cnts, hier = cv2.findContours(dilation.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# cv2.drawContours(resized, cnts, -1, (0, 255, 0), 3)

for i in xrange(len(cnts)):
    if cv2.contourArea(cnts[i]) > 20:
        if hier[i][2][1] < 0:
            cv2.drawContours(resized, [cnts[i]], -1, (0, 255, 0), 3)

cv2.imshow("dilation", dilation)
cv2.imshow("resized", resized)
cv2.waitKey(0)
