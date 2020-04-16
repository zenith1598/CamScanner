import numpy as np
import cv2 as cv

filename = r'C:\Users\raman bansal\Pictures\testimage.jpg'
img = cv.imread(filename)

# Converting image to monochrome. Then only find contours would work.
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(grayImg, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, 1, 2)

# obtain the first 2 points of contours
cntx1 = contours[0][0]
cntx = contours[0][1]
cnt = contours[0]
M = cv.moments(cnt)

# The function cv.moments() gives a dictionary of all moment values calculated.

# print(M)

area = cv.contourArea(cnt)  # Contour area is given by the function cv.contourArea() or from moments, M['m00'].

perimeter = cv.arcLength(cnt,
                         True)  # It is also called arc length. It can be found out using cv.arcLength() function. Second argument specify whether shape is a closed contour (if passed True), or just a curve.

# From this moments, you can extract useful data like area, centroid etc. Centroid is given by the relations, Cx=M10M00 and Cy=M01M00. This can be done as follows:
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

print("Centroid " + str(cx) + " " + str(cy))
print("Area " + str(area))
print("Perimeter " + str(perimeter))
width = 1.367
length = 1.463  # after calculation on paper

((x, y), (w, h), angle) = cv.minAreaRect(cnt)
# x,y  are the coordinates of center


print("Top Left Corner " + str(0) + "," + str(width))

# top right corner

print("Top Right Corner " + str(length) + "," + str(width))

# bottom left corner


print("Bottom Left Corner " + str(0) + "," + str(0))
l2 = 0.0

# bottom right corner
print("Bottom right corner " + str(length) + "," + str(0))
l3 = 0.0
# have taken bottom left corner as origin