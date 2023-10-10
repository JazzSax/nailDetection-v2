import cv2
from Utils.getAspectRatio import *

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def getNailShape(c):
    isNail = False

    #Detect shape
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True) #can change multiplier on perimeter

    #check for unnecessary shapes 
    if (len(approx) >= 6 and len(approx) <= 11):
        #print("Area: ", str(cv2.contourArea(c)))
        #print("Approx Len: ", str(len(approx)))
        #nailSize = getAspectRatio(c)
        shape = "a nail: " #+ nailSize
        isNail = True
    else:
        #print("Not a nail found")
        #print("Approx Len: ", str(len(approx)))
        shape = "Not a nail"
        isNail = False
    
    #print(shape)
    return (shape, isNail)
