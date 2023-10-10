import cv2
import numpy as np
import imutils

#read file ./_Imgs/20231008_102117.jpg ./_Images-standard/20231007_160450.jpg ./_Images/20231007_160450.jpg
fra = cv2.imread('./_Imgs/20231008_102721.jpg')
fra = imutils.resize(fra, height=600)
cv2.imshow("Original Image", fra)

# convert to gray
gray = cv2.cvtColor(fra, cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)[1]

# morphology edgeout = dilated_mask - mask
# morphology dilate
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel)

# get absolute difference between dilate and thresh
diff = cv2.absdiff(dilate, thresh)

# invert
edges = 255 - diff


# display it
cv2.imshow("thresh", thresh)
cv2.imshow("dilate", dilate)
cv2.imshow("diff", diff)
cv2.imshow("edges", edges)
cv2.waitKey(0)