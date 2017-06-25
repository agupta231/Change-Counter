import cv2

class shape_detector:
    def __init__(self):
        pass

    def detect(self, c):
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)

        if len(approx) == 3:
            return "triangle"
        elif len(approx) == 4:
            return "quad"
        elif len(approx) == 5:
            return "pentagon"
        elif len(approx) == 6:
            return