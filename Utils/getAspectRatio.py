#output should be short, wide, long etc FOR TESTING PURPOSE ONLY
'''
reference

https://www.tutorialspoint.com/how-to-compute-the-aspect-ratio-of-an-object-in-an-image-using-opencv-python
'''
import cv2

#MODULE TO BE REMOVED; just for testing
def getAspectRatio(cnt):
    x, y, w, h = cv2.boundingRect(cnt)
    ratio = float(w)/h
    nailRatio = ""

    if ratio >= 0.90 and ratio <= 1.10:
        nailRatio = "small almost equal sides"
    elif ratio >= 1.11:
        nailRatio = "wide nail"
    else: #ratio <= 0.89
        nailRatio = "long nail"
    
    return nailRatio