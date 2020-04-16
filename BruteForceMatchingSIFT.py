import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img2 = cv.imread('C:\opencvpictures\Image2.jpg', cv.IMREAD_GRAYSCALE)

img1 = cv.imread('C:\opencvpictures\Template.jpg', cv.IMREAD_GRAYSCALE)
# cv.imshow("Main Image",img2)
# cv.imshow("Logo",img1)
# cv.waitKey(0)
# cv.destroyAllWindows()


# sift=cv.xfeatures2d.SIFT_create()

# surf = cv.xfeatures2d.SURF_create()


orb = cv.xfeatures2d.SURF_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

print("KeyPoints of logo " + str(kp1))
# print("KeyPoints of main image " + str(kp2))

# for i in des1:
#   print(i)

# for j in des2:
#   print(j)

# Brute Force Matching
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# for i in matches:
# print(i)

# taking out the mean of the distance
# sum = 0
# for m in matches:
# sum = sum + m.distance

# end of loop

# mean = sum / len(matches)


good = []

for m, n in matches:

    # print(m.distance)
    # print(n.distance)
    if m.distance < 0.5 * n.distance:
        good.append([m])

        # good array contains the best matches.

        ' Lets us find the points of the best matches'

        # print(matches)
    # print(good)
points = []
# for i, j in matches:
#   point = kp2[i.trainIdx].pt
#  points.append(point)
# print(point)


for i in good:
    point = kp2[i[0].trainIdx].pt
    points.append(point)
    print(point)

# sumX = 0
# sumY = 0
# for i in range(len(points)):
#   sumX = sumX + points[i][0]
#  sumY = sumY + points[i][1]

# centreX = sumX / len(points)
# centreY = sumY / len(points)

# print("Centre point is " + str(centreX) + " , " + str(centreY))

# cv.circle(img2, (int(centreX), int(centreY)), 1, 4, 20)


# will find te minimum value of x

minX = points[0][0]
minY = points[0][1]

for i in range(len(points)):
    if (points[i][0] < minX):
        minX = points[i][0]
    if (points[i][1] < minY):
        minY = points[i][1]

maxX = points[0][0]
maxY = points[0][1]

for i in range(len(points)):
    if (points[i][0] > maxX):
        maxX = points[i][0]
    if (points[i][1] > maxY):
        maxY = points[i][1]

print("Minimum X  " + str(minX))
print("Minimum Y " + str(minY))

cv.circle(img2, (int(minX), int(minY)), 1, 4, 20)

cv.circle(img2, (59, 78), 1, 4, 4)  # (59,78) is the closest to (34,48)
cv.circle(img2, (137, 79), 1, 4, 4)  # (137,79) is the closest to (176,48) top right
cv.circle(img2, (49, 122), 1, 4, 4)  # (49,122) is the closest to (34,147) bottom left
cv.circle(img2, (149, 130), 1, 4, 4)  # (149,130) is the closest to (176,147) bottom right
cv.imshow("Image", img2)
# matches=sorted(matches,key=lambda x:x.distance)

# matching_result= cv.drawMatches(img1,kp1,img2,kp2,matches[:10],None)

# print(len(matches))

# for m in matches:
#   print(m.distance)

img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
# it does the line matching. No required in our case

cv.imshow("Match", img3)
cv.waitKey(0)
cv.destroyAllWindows()
