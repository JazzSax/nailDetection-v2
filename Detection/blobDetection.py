
from cv2 import SimpleBlobDetector_Params
from cv2 import SimpleBlobDetector_create
def getBlob(width, height, mask):
    #BLOB DETECTION
    params = SimpleBlobDetector_Params()
    params.filterByArea = True     #filter the image based on area
    params.minArea = int(height* width/500)   #minimum area to be detected
    params.maxArea = int((height * width))   #max area to be detected 
    params.filterByCircularity = True
    params.minCircularity = 0.1   #filter the image by its circularity set on mincircularity
    params.filterByConvexity = True
    params.minConvexity = 0.2 #filter the image by its convexity set on minconvexity
    params.filterByInertia = True
    params.minInertiaRatio = 0.19  #fitler the image by its elongation set on min inertia

    detector = SimpleBlobDetector_create(params)
    key_points = detector.detect(255-mask)
    return key_points