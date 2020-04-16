import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'C:\opencvpictures\Image2-10.jpg', 0)
img2 = img.copy()
template = cv.imread(r'C:\opencvpictures\Template.jpg', 0)
w, h = template.shape[::-1]
W, H = img.shape[::-1]
# width and height of main image


img3 = img2.copy()
method = eval('cv.TM_CCOEFF')
print("Height og image " + str(H))
print("Width og image " + str(W))

# Apply template Matching
res = cv.matchTemplate(img3, template, method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

bottom_right = (top_left[0] + w, top_left[1] + h)
bottom_left = (top_left[0],top_left[1] + h)
name_left= (top_left[0],int(((top_left[1] + h)*1.8)))



print("Top Left Coordinate = " + str(top_left[0]) + "," + str(top_left[1]))
print("Top Right Coordinate = " + str(top_left[0] + w) + "," + str(top_left[1]))
print("Bottom left Coordinate = " + str(top_left[0]) + "," + str(top_left[1] + h))
print("Bottom right coordinate = " + str(bottom_right[0]) + "," + str(bottom_right[1]))
cv.rectangle(img, top_left, bottom_right, 10, 10)

cv.rectangle(img,name_left,((int(name_left[0] * 25)),(int(name_left[1]*1.25))),10,10)
# let us draw an ellipse





plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

plt.show()
