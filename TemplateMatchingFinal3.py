import cv2 as cv
import numpy as nv
from matplotlib import pyplot as plt

image = cv.imread('C:\EXAMPLES\OpenCV\image-bestcase.jpg', 0)
logo = cv.imread('C:\EXAMPLES\OpenCV\logo-1.jpg', 0)
logo_2 = cv.imread('C:\EXAMPLES\OpenCV\logo-2.jpg', 0)
logo_3 = cv.imread('C:\EXAMPLES\OpenCV\logo-3.jpg', 0)
img2 = image.copy()
w, h = logo.shape[:: -1]
W, H = logo_2.shape[:: -1]
W_3, H_3 = logo_3.shape[::-1]


method = eval('cv.TM_CCOEFF')

res = cv.matchTemplate(img2, logo, method)
res_2 = cv.matchTemplate(img2, logo_2, method)
res_3 = cv.matchTemplate(img2, logo_3, method)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

min_val_2, max_val_2, min_loc_2, max_loc_2 = cv.minMaxLoc(res_2)

min_val_3, max_val_3, min_loc_3, max_loc_3 = cv.minMaxLoc(res_3)

top_left = max_loc
top_left_2 = max_loc_2
top_left_3 = max_loc_3

bottom_right = (top_left[0] + w, top_left[1] + h)
bottom_right_2 = (top_left_2[0] + W_3, top_left_2[1] + H_3)
bottom_left_2 = (top_left_2[0], bottom_right_2[1])
bottom_right_3 = (top_left_3[0] + W_3, top_left_3[1] + H_3)
cv.rectangle(image, top_left, bottom_right, 10, 4)
cv.rectangle(image, top_left_2, bottom_right_2, 10, 4)
cv.rectangle(image, top_left_3, bottom_right_3, 10, 4)
cv.circle(image, top_left, 2, 4, 5)
cv.circle(image, bottom_right, 2, 4, 5)

diff_x = top_left_3[0] - top_left_2[0];
diff_y = top_left_2[1] - top_left[1]
page_width = top_left_2[0] + int(diff_x * 2.996)
page_height = bottom_right_2[1] - top_left[1]

cv.circle(image, (page_width, top_left_2[1]), 2, 2, 2)
# cv.rectangle(image,top_left,(page_width,bottom_right_2[1]),10,5)
# cv.line(image,top_left,bottom_left_2,2,2,2)
# cv.line(image,bottom_left_2,((bottom_left_2[0]+page_width),bottom_left_2[1]),2,2,2)

cv.circle(image, ((int(top_left[0] + page_width / 10 * 1.85), int(top_left[1] + page_height / 100 * 1.2))), 2, 2, 2)

sign_height = page_height / 12
sign_width = page_width / 4.75
sign_gap = (page_width / 4.2 - sign_width)
cv.rectangle(image, (int(top_left[0] + page_width / 10 * 1.85), int(top_left[1] + page_height / 100 * 1.2)),
             (int(top_left[0] + page_width / 10 * 6), int(top_left[1] + page_height / 50 * 2)), 5, 10)
# UMRN
cv.rectangle(image, (int(top_left[0] + page_width / 10 * 6.1), top_left[1]),
             (int(top_left[0] + page_width / 10 * 8), int(top_left[1] + page_height / 50 * 2)), 5, 10)  # date

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 2.7), int(top_left[1] + page_height / 50 * 4)),
             (int(top_left[0] + page_width / 10 * 8.4), int(top_left[1] + page_height / 50 * 5)), 5, 10)
# Account No

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 1.7), int(top_left[1] + page_height / 50 * 5.35)),
             (int(top_left[0] + page_width / 10 * 3.5), int(top_left[1] + page_height / 50 * 6.5)), 5, 10)
# Bank Name

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 3.8), int(top_left[1] + page_height / 50 * 5.15)),
             (int(top_left[0] + page_width / 10 * 6.15), int(top_left[1] + page_height / 50 * 6.1)), 5, 10)
# IFSC Code

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 6.5), int(top_left[1] + page_height / 50 * 5.)),
             (int(top_left[0] + page_width / 10 * 8.5), int(top_left[1] + page_height / 50 * 6)), 5, 10)
# MICR Code


cv.rectangle(image, (int(top_left[0] + page_width / 10 * 3), int(top_left[1] + page_height / 10 * 2.2)),
             (int(top_left[0] + page_width / 10 * 4.6), int((top_left[1] + page_height / 10 * 2.55))), 5,
             10)  # main sign 1

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 4.8), int(top_left[1] + page_height / 10 * 2.2)),
             (int(top_left[0] + page_width / 10 * 6.4), int((top_left[1] + page_height / 10 * 2.55))), 5,
             10)  # main sign 2

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 6.8), int(top_left[1] + page_height / 10 * 2.2)),
             (int(top_left[0] + page_width / 10 * 8.4), int((top_left[1] + page_height / 10 * 2.55))), 5,
             10)  # main sign 3

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 3), int(top_left[1] + page_height / 10 * 2.6)),
             (int(top_left[0] + page_width / 10 * 4.6), int((top_left[1] + page_height / 10 * 2.9))), 5, 10)  # name 1

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 4.8), int(top_left[1] + page_height / 10 * 2.6)),
             (int(top_left[0] + page_width / 10 * 6.4), int((top_left[1] + page_height / 10 * 2.9))), 5, 10)  # name 2

cv.rectangle(image, (int(top_left[0] + page_width / 10 * 6.8), int(top_left[1] + page_height / 10 * 2.6)),
             (int(top_left[0] + page_width / 10 * 8.4), int((top_left[1] + page_height / 10 * 2.9))), 5, 10)  # name 3

cv.rectangle(image, (top_left[0], int(top_left[1] + page_height / 4 * 3.25)),
             (int(top_left[0] + sign_width), int((top_left[1] + page_height / 4 * 3.05) + sign_height)), 5, 10)  # sign1
cv.rectangle(image, (int(top_left[0] + sign_width + sign_gap), int(top_left[1] + page_height / 4 * 3.05)),
             (int(top_left[0] + 2 * sign_width + sign_gap), int((top_left[1] + page_height / 4 * 3.05) + sign_height)),
             5, 10)  # sign2
cv.rectangle(image, (int(top_left[0] + sign_width * 2 + sign_gap * 2), int(top_left[1] + page_height / 4 * 3.05)),
             (int(top_left[0] + 3 * sign_width + sign_gap * 2),
              int((top_left[1] + page_height / 4 * 3.05) + sign_height)),
             5, 10)  # sign3
cv.rectangle(image, (int(top_left[0] + sign_width * 3 + 3 * sign_gap), int(top_left[1] + page_height / 4 * 3.05)), (
    int(top_left[0] + 4 * sign_width + 3 * sign_gap), int((top_left[1] + page_height / 4 * 3.05) + sign_height)), 5,
             10)  # sign4
cv.line(image,top_left,bottom_left_2,3,4)

bottom_logo_dist=bottom_right_3[0]-bottom_left_2[0]

cv.circle(image,(int(top_left_2[0]-page_width/50*2),top_left_2[1]),4,1,100)
# print(min_val, max_val, min_loc, max_loc)
# print(W,H)
# print(w,h)
# print(W,H)
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title("Image")
plt.show()