from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
from Utils.sizeComputation import *


def getCoinContour(img, width, height):
    # Convert to HSV format and color threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #included with edge
    # Apply blur technique
    gray = cv2.medianBlur(gray, 11)
    edged = cv2.Canny(gray, 0, 255)
    #eroded = cv2.erode(edged, None, iterations=4) #eroding loses the object
    dilated = cv2.dilate(edged, None, iterations=5)

    # Get the contours from your thresholded image
    (contour, hier) = cv2.findContours(dilated.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
   
    (cnts, _) = contours.sort_contours(contour)

    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        # test if contour touches border of image
        if x == 0 or y == 0 or x+w == width or y+h == height:
            print("found contour on border")
            continue
        
        return c


def drawCoin(orig, c, referenceSize):
    pixelsPerMetric = None

    box = cv2.minAreaRect(c)
    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")

    # order the points in the contour; tl, tr, br, bl order, then draw the outline of the rotated bounding box
    box = perspective.order_points(box)
    cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
    
    # loop over the original points and draw them
    for (x, y) in box:
        cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

    # unpack the ordered bounding box, then compute the midpoint
    (tl, tr, br, bl) = box
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)

    # draw the midpoints on the image
    cv2.circle(orig, (int(tltrX), int(tltrY)), 3, (255, 0, 0), -1)
    cv2.circle(orig, (int(blbrX), int(blbrY)), 3, (255, 0, 0), -1)
    cv2.circle(orig, (int(tlblX), int(tlblY)), 3, (255, 0, 0), -1)
    cv2.circle(orig, (int(trbrX), int(trbrY)), 3, (255, 0, 0), -1)
    
    # draw lines between the midpoints
    cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
    cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)
    
    # compute the Euclidean distance between the midpoints
    distA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    distB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    
    # compute pixel per metric in inches (to update change)
    # (in this case, inches)
    if pixelsPerMetric is None:
        pixelsPerMetric = distB / referenceSize
    
    # compute the dimensions of the object
    dimA = distA / pixelsPerMetric
    dimB = distB / pixelsPerMetric

    print("Length: {:.2f}mm".format(dimA))
    print("Width: {:.2f}mm".format(dimB))

    # draw the object sizes on the image
    cv2.putText(orig, "{:.1f}mm".format(dimA), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
    cv2.putText(orig, "{:.1f}mm".format(dimB), (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
    cv2.imshow("Image", orig)
    cv2.waitKey(0)
    return pixelsPerMetric
