import cv2
import numpy as np
import imutils
def nothing(x):
    pass

# Load imagepics\pics\20231007_140959.jpg _Images-standard\20231007_155811.jpg 
# NEW DATA SET ./_Imgs/20231008_102117.jpg
image = cv2.imread('./_Imgs/20231008_102721.jpg')
image = imutils.resize(image, height = 400)
# Create a window

cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('Lower', 'image', 0, 255, nothing)
cv2.createTrackbar('Upper', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('Lower', 'image', 0)
cv2.setTrackbarPos('Upper', 'image', 255)

# Initialize HSV min/max values
Lower = 0
Upper = 0

while(1):
    # Get current positions of all trackbars
    Lower = cv2.getTrackbarPos('Lower', 'image')
    Upper = cv2.getTrackbarPos('Upper', 'image')

    # Set minimum and maximum HSV values to display
    lower = Lower
    upper = Upper
    # Convert to HSV format and color threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #included with edge
    # Apply blur technique
    gray = cv2.medianBlur(gray, 11)
    edged = cv2.Canny(gray, lower, upper)
    # Display result image
    cv2.imshow('image', edged) #or thresh depending on use case
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()