import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.cvtColor(cv2.imread("C:\opencvpictures\Image2.jpg"), cv2.COLOR_BGR2RGB)

# Now to use canny edge detection


# height = 800
# rat = height / image.shape[0]
# img = cv2.resize(image, (int(rat * image.shape[1]), height))
# cv2.imshow("resized image", img)

""""Resize and convert to grayscale"""""

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Bilateral filter preserve edges
img = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("First Image", img)
# Create black and white image based on adaptive threshold
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 4)
cv2.imshow("Second Image", img)
# Median filter clears small details
#img = cv2.medianBlur(img, 11)
cv2.imshow("Third Image",img)
# Add black border in case that page is touching an image border
img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[0, 0, 0])
cv2.imshow("Fourth Image", img)
edges = cv2.Canny(img, 200, 250)

# Getting contours
im2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Finding contour of biggest rectangle
#  Otherwise return corners of original image
#  Don't forget on our 5px border!
height = edges.shape[0]
width = edges.shape[1]
MAX_COUNTOUR_AREA = (width - 10) * (height - 10)

# Page fill at least half of image, then saving max area found
maxAreaFound = MAX_COUNTOUR_AREA * 0.5

# Saving page contour
pageContour = np.array([[5, 5], [5, height - 5], [width - 5, height - 5], [width - 5, 5]])

for cnt in contours:
    # Simplify contour
    perimeter = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.03 * perimeter, True)
    # Page has 4 corners and it is convex
    #  Page area must be bigger than maxAreaFound
    if (len(approx) == 4 and cv2.isContourConvex(approx) and maxAreaFound < cv2.contourArea(
            approx) < MAX_COUNTOUR_AREA):
        maxAreaFound = cv2.contourArea(approx)
        pageContour = approx

        # Perspective Transformation

        pts = pageContour[:, 0]

        """ Sort corners: top-left, bot-left, bot-right, top-right """
        # Difference and sum of x and y value

        diff = np.diff(pts, axis=1)
        summ = pts.sum(
            axis=1)
        # Top-left point has smallest sum...
        # np.argmin()
        # returns INDEX of min
        pageContour = np.array([pts[np.argmin(summ)],
                                pts[np.argmax(diff)],
                                pts[np.argmax(summ)],
                                pts[np.argmin(diff)]])

        """ Offset contour, by 5px border """

        # Matrix addition

        pageContour += (-5, -5)
        # if value < 0 => replace it by 0
        pageContour[pageContour < 0] = 0

    # Recalculate to original scale - start Points
    sPoints = pageContour.dot(img.shape[0] / 800)

    # Using Euclidean distance	# Calculate maximum height (maximal length of vertical edges) and width
    height = max(np.linalg.norm(sPoints[0] - sPoints[1]),
                 np.linalg.norm(sPoints[2] - sPoints[3]))
    width = max(np.linalg.norm(sPoints[1] - sPoints[2]), np.linalg.norm(sPoints[3] - sPoints[0]))

    # Create target points
    tPoints = np.array([[0, 0], [0, height], [width, height], [width, 0]], np.float32)

    # getPerspectiveTransform() needs float32
    if sPoints.dtype != np.float32:
        sPoints = sPoints.astype(np.float32)

        # Wrapping perspective
        M = cv2.getPerspectiveTransform(sPoints, tPoints)
    newImage = cv2.warpPerspective(img, M, (int(width), int(height)))

    """(don't forget to convert colors back to BGR)"""

    cv2.cvtColor(newImage, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Final Image", newImage)
    cv2.waitKey()
