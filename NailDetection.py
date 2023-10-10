from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from imutils import is_cv2
import numpy as np
import argparse
import cv2
import Detection.coinDetection as coinDetection
from Utils.nailDescription import Nail
from Utils.displayWindow import showWindow
from Utils.sizeComputation import *
from Detection.blobDetection import *
import maskSettings as SETTINGS
#Change depending on reference object size




#read file ./_img-colormatched/20231007_160450.jpg ./_img-colormatched/20231007_143437.jpg ./_img-colormatchedv2/20231007_143437.jpg
fra = cv2.imread('./_Imgs/20231008_102721.jpg')

fra = SETTINGS.resizeImage(fra)
#showWindow("Original Image", fra)

# Get the dimensions of the image
height, width, channels = fra.shape

# Apply blur technique
src = cv2.medianBlur(fra, 11)

# Convert the image to HSV
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#showWindow("HSV", hsv)



maskBG = cv2.inRange(hsv, SETTINGS.BG_MIN, SETTINGS.BG_MAX)
maskPink = cv2.inRange(hsv, SETTINGS.PINK_MIN, SETTINGS.PINK_MAX)
maskNailWhite = cv2.inRange(hsv, SETTINGS.NAILWHITE_MIN, SETTINGS.NAILWHITE_MAX)
maskNail = cv2.bitwise_or(maskPink, maskNailWhite)
maskNail = cv2.dilate(maskNail, None, iterations=2)

#mask = maskCombine - maskBG
mask = cv2.subtract(maskNail, maskBG)
#showWindow("Combined Mask minus BG", mask)

# Decrease the size of the mask (erosion)
mask = cv2.erode(mask, None, iterations=11)
#showWindow("Erode", mask)

# Increase the size of the mask (dilation)
mask = cv2.dilate(mask, None, iterations=8)
showWindow("Dilate", mask)

#Get Keypoints if blob (nail) is found
key_points = getBlob(width, height, mask)

widths = []
lengths = []
if len(key_points) == 0:
    print("no nails detected")
else:
    
    minArea = 200
    maxArea = 50000

    output = fra.copy()
    # Get the contours from your thresholded image
    (contour, hier) = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # sort the contours from left-to-right and initialize the
    # 'pixels per metric' calibration variable 
    (cnts, _) = contours.sort_contours(contour)

    coinContour = coinDetection.getCoinContour(fra, width, height)
    pixelsPerMetric = coinDetection.drawCoin(fra.copy(), coinContour, SETTINGS.referenceSize)

    for c in cnts:

        #Check if contour is too small or too big
        if cv2.contourArea(c) < minArea or cv2.contourArea(c) > maxArea:
            print("Area is", cv2.contourArea(c))
            continue

        #Use this shape somewhere; check if contour is a nail or nail-like
        (shape, isNail) = getNailShape(c)

        if not isNail:
            continue
        print("")
        
        x,y,w,h = cv2.boundingRect(c)
        # test if contour touches border of image
        if x == 0 or y == 0 or x+w == width or y+h == height:
            print('region touches the sides')
            continue

        #Get center
        M = cv2.moments(c)
        (cX, cY) = (0, 0)
        if M["m00"] != 0:
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
        c = c.astype("int")
        
        orig = fra.copy()
        mask2 = mask.copy()
        #convexHull = cv2.convexHull(c)
        #cv2.drawContours(orig, [convexHull], -1, (255, 0, 0), 2)
        
        ###Size Detection Start - compute the rotated bounding box of the contour
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if is_cv2() else cv2.boxPoints(box)
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
        
        # compute pixel per metric in mm (to update change)
        # (in this case, mm)
        if pixelsPerMetric is None:
            pixelsPerMetric = distB / SETTINGS.referenceSize
        
        # compute the dimensions of the object
        dimA = distA / pixelsPerMetric
        dimB = distB / pixelsPerMetric
        
        lengths.append(dimA)
        widths.append(dimB)
       
        print("Length: {:.2f}mm".format(dimA))
        print("Width: {:.2f}mm".format(dimB))

        # draw the object sizes on the image
        cv2.putText(orig, "{:.1f}mm".format(dimA), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
        cv2.putText(orig, "{:.1f}mm".format(dimB), (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
        cv2.imshow("Image", orig)
        cv2.imshow("mask2",mask2)
        
        cv2.waitKey(0)


n = Nail(widths,lengths)
nailSize,width,height = n.nailDescriptionOnSize() 
cv2.putText(orig, nailSize, (int(50), int(50)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
cv2.putText(orig, f"width of the nail is: {width}%", (int(50), int(70)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
cv2.putText(orig, f"height of the nail is: {height}%", (int(50), int(90)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
cv2.imshow("Image", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()