import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r'C:\opencvpictures\Image2.jpg', 0)
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

print("Top Left = " + str(top_left))

bottom_right = (top_left[0] + w, top_left[1] + h)
bottom_left = (top_left[0], top_left[1] + h)
name_left = (top_left[0], int(((top_left[1] + h) * 1.8)))
print("Bottom Left " + str(bottom_left))
print("Bottom Right " + str(bottom_right))


p1_top_left = (top_left[0] * 40, int(((top_left[1] + h) * 1.8)))

print("Top Left Coordinate = " + str(top_left[0]) + "," + str(top_left[1]))
print("Top Right Coordinate = " + str(top_left[0] + w) + "," + str(top_left[1]))
print("Bottom left Coordinate = " + str(top_left[0]) + "," + str(top_left[1] + h))
print("Bottom right coordinate = " + str(bottom_right[0]) + "," + str(bottom_right[1]))
cv.rectangle(img, top_left, bottom_right, 10, 10)  # logo
# cv.rectangle(img, p1_top_left, bottom_right, 10, 10)     #proposal number1
# cv.rectangle(img, top_left, bottom_right, 10, 10)     #proposal no 2
# cv.rectangle(img, top_left, bottom_right, 10, 10)     #txnID

cv.rectangle(img, name_left, ((int(name_left[0] * 25)), (int(name_left[1] * 1.25))), 10, 5)  # name
cv.rectangle(img, ((top_left[0] * 30), top_left[1] - 10), ((bottom_left[0] * 45), bottom_left[1] - 40), 10,
             5)  # proposalno1
cv.rectangle(img, ((top_left[0] * 30), bottom_left[1] - 15), ((bottom_left[0] * 45), bottom_left[1] + 28), 10,
             5)  # proposalno2
cv.rectangle(img, ((top_left[0] * 30), bottom_left[1] + 45), ((bottom_left[0] * 45), bottom_left[1] + 100), 10,
             5)  # txnID
cv.rectangle(img, ((top_left[0] + 10), (top_left[1] * 28 + 5)), ((top_left[0] * 12), (top_left[1] * 28 + 75)), 10,
             5)  # place

cv.rectangle(img, ((top_left[0] * 28 - 25), (top_left[1] * 28 - 10)), ((top_left[0] * 45), (top_left[1] * 28 + 45)), 10,
             5)  # sign2
cv.rectangle(img, ((top_left[0] * 13), (top_left[1] * 27 + 70)), ((top_left[0] * 22), (top_left[1] * 28 + 75)), 10,
             5)  # sign1
cv.rectangle(img, ((top_left[0] * 13), (top_left[1] * 27 + 30)), ((top_left[0] * 22), (top_left[1] * 28 + 25)), 10,
             5)  # date

plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'),
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

plt.show()
