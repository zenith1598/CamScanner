import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'C:\opencvpictures\Image.jpg', 0)
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

# for i in range(1, 9):
M = cv.getRotationMatrix2D((w / 2, h / 2), -90, 1)
# angle = angle + 10

dst = cv.warpAffine(template, M, (h, w))  # now height and width of the rotated image will be reversed.
cv.imshow("After Rotation", dst)

img4 = dst.copy()

res = cv.matchTemplate(img3, dst, method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

bottom_right = (top_left[0] + h, top_left[1] + w)

print("Top Left Coordinate = " + str(top_left[0]) + "," + str(top_left[1]))
print("Top Right Coordinate = " + str(top_left[0] + h) + "," + str(top_left[1]))
print("Bottom left Coordinate = " + str(top_left[0]) + "," + str(top_left[1] + w))
print("Bottom right coordinate = " + str(bottom_right[0]) + "," + str(bottom_right[1]))
cv.rectangle(img, top_left, bottom_right, 10, 10)  # logo

plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

plt.show()
