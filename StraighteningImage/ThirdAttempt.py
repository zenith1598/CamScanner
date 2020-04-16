import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("C:\opencvpictures\Exp1.jpg")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Using RETR_EXTERNAL gives only parent contours and leaves behind the child contours

cnt = contours[0]
(x, y), (w, h), angle = cv.minAreaRect(cnt)
print(angle)

# Now we will calculate 4 corner points of bounding rectangle and pass it to an array
pts_src = np.array([[x + 6, y + 2], [x + w - 40, y], [x + 8, y + h - 8], [x + w - 10, y + h]])

# ---- 4 corner points of the black image you want to impose it on
pts_dst = np.array([[x, y], [x + w, y], [x, y + h], [x + w, y + h]])
# ---- forming the black image of specific size
im_dst = np.zeros((int(h), int(w), 3), np.uint8)
# cv.imshow("Intermediate", im_dst)

# ---- Framing the homography matrix
height, status = cv.findHomography(pts_src, pts_dst)


# ---- transforming the image bound in the rectangle to straighten
im_out = cv.warpPerspective(img, height, (im_dst.shape[1], im_dst.shape[0]))
plt.subplot(122), plt.xticks([]), plt.yticks([]), plt.imshow(im_out)
plt.title("Croped Image")
plt.show()

cv.waitKey()
