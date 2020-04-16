MIN_CONTOUR_AREA = 100

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30


class ContourWithData():
    # member variables ############################################################################
    npaContour = None  # contour
    boundingRect = None  # bounding rect for contour
    intRectX = 0  # bounding rect top left corner x location
    intRectY = 0  # bounding rect top left corner y location
    intRectWidth = 0  # bounding rect width
    intRectHeight = 0  # bounding rect height
    fltArea = 0.0  # area of contour

    def calculateRectTopLeftPointAndWidthAndHeight(self):  # calculate bounding rect info
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight

    def checkIfContourIsValid(self):  # this is oversimplified, for a production grade program
        if self.fltArea < MIN_CONTOUR_AREA: return False  # much better validity checking would be necessary
        return True
