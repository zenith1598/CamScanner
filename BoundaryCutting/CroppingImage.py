import cv2 as cv
import numpy as np

img = cv.imread("C:\opencvpictures\Image2.jpg")
height = 800
rat = height / img.shape[0]
img = cv.resize(img, (int(rat * img.shape[1]), height))
fromCenter = True
showCrosshair = True
r = cv.selectROI("Image", img, fromCenter, showCrosshair)

imCrop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

cv.imshow("Image", imCrop)
cv.waitKey()
