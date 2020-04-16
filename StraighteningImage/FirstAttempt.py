import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\opencvpictures\Image.jpg")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rows, colls, ch = img.shape
ret, thresh = cv.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
""""im2 = modified image"""

# cv.imshow("Modified Image", im2)
#cv.waitKey()

# Rotated Rectangle
i = 0
while (i < len(contours)):
    cnt = contours[i]
    (x, y), (width, height), angleOfRotation = cv.minAreaRect(cnt) # For rotated image.
    M = cv.getRotationMatrix2D((colls / 2, rows / 2), -angleOfRotation, 1)
    dst = cv.warpAffine(img, M, (colls, rows))

    cv.imshow("Rotated Image", dst)

    plt.subplot(122), plt.imshow(dst)
    plt.title('Angle of rotation = ' + str(angleOfRotation))
    plt.show()
    i = i + 1

# print("Angle of Rotation is = " + str(angleOfRotation))
