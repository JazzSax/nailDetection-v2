
from cv2 import namedWindow
from cv2 import moveWindow
from cv2 import imshow
def showWindow(winname, i):
    namedWindow(winname)        # Create a named window
    moveWindow(winname, 500, 100)   # Move it to (x,y)
    imshow(winname,i)
