import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("C:\opencvpictures\Image.jpg")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
h, w = img.shape[:2]
ret, thresh = cv.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
""""im2 = modified image"""

# cv.imshow("Modified Image", im2)


# Rotated Rectangle
i = 0
cnt = contours[0]

(x, y), (width, height), angleOfRotation = cv.minAreaRect(cnt)  # For rotated image.
M = cv.getRotationMatrix2D((w / 2, h / 2), -angleOfRotation, 1)
print("Angle of rotation = " + str(angleOfRotation))
dst = cv.warpAffine(img, M, (w, h))

# cv.imshow("Rotated Image", dst)

plt.subplot(121), plt.imshow(img)
plt.title('Original Image ')
plt.show()

plt.subplot(122), plt.imshow(dst)
plt.title('Angle of rotation = ' + str(angleOfRotation))
plt.show()
