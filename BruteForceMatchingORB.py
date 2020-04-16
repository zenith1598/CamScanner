# here we will use ORB descriptor.
# It takes descriptor of one set of image and matches with the other set using some distance calculations.
# The best one is returned.


import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt

img1 = cv2.imread(r'C:\opencvpictures\Template.jpg', 0)  # query image
img2 = cv2.imread(r'C:\opencvpictures\Image.jpg', 0)  # main image

# Initiate ORB detector
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING,
                   crossCheck=True)  # crossCheck= True,  means that both the queryimage and the mainimage are compared on the basis of descriptors.

# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)

# Draw first k  matches. here k
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10000], None, flags=2)
# None is for Output image. There are some errors in opencv documentation which I have duly rectified here in the code.

plt.imshow(img3), plt.show()
