from numpy import array 
from imutils import resize


PINK_MIN = array([0, 33, 123])
PINK_MAX = array([7, 139, 255])
NAILWHITE_MIN = array([8, 64, 124])
NAILWHITE_MAX = array([16, 113, 156])
BG_MIN = array([8, 0, 158])
BG_MAX = array([179, 255, 255])
referenceSize =  23 #if 23mm new 1 peso coin

def resizeImage(image):
    return resize(image,height=600)


'''
    ------
    #new data set new mask ##########CURRENTLY USING THIS MASK
    COIN_MIN = np.array([9, 5, 0])
    COIN_MAX = np.array([23, 82, 175])
    COINHIGH_MIN = np.array([3, 17, 17])
    COINHIGH_MAX = np.array([25, 126, 75])

    PINK_MIN = np.array([0, 33, 123])
    PINK_MAX = np.array([7, 139, 255])
    NAILWHITE_MIN = np.array([8, 64, 124])
    NAILWHITE_MAX = np.array([16, 113, 156])

    BG_MIN = np.array([8, 0, 158])
    BG_MAX = np.array([179, 255, 255])

    WORKING kinda:
    ./_Imgs/20231008_102721.jpg
    ./_Imgs/20231008_102543.jpg
    ./_Imgs/20231008_102516.jpg
    ./_Imgs/20231008_102440.jpg

    got only one nail:
    ./_Imgs/20231008_102117.jpg
    ./_Imgs/20231008_102238.jpg

    ./_img-colormatched/20231007_143437.jpg
    ./_img-colormatched/20231007_155732.jpg - only 1 finger
    ./_img-colormatched/20231007_160355.jpg - only 2 fingers
    ./_img-colormatched/20231007_160450.jpg - scuffed

    ./_img-colormatchedv2/20231007_143437.jpg - coin not that accurate
    ./_img-colormatchedv2/20231007_142624.jpg - maybe but sideways
    ./_img-colormatchedv2/20231007_140959.jpg - bit wide
    ./_img-colormatchedv2/20231007_140959.jpg - bit big
    everything else doesnt seem to work
'''

'''
```
------
    #new data set new mask
    COIN_MIN = np.array([9, 5, 0])
    COIN_MAX = np.array([23, 82, 175])
    COINHIGH_MIN = np.array([3, 17, 17])
    COINHIGH_MAX = np.array([25, 126, 75])

    PINK_MIN = np.array([0, 33, 123])
    PINK_MAX = np.array([7, 139, 255])
    NAILWHITE_MIN = np.array([8, 64, 124])
    NAILWHITE_MAX = np.array([16, 113, 156])

    BG_MIN = np.array([8, 0, 158])
    BG_MAX = np.array([179, 255, 255])

    WORKING kinda:
    ./_Imgs/20231008_102721.jpg
    ./_Imgs/20231008_102543.jpg
    ./_Imgs/20231008_102516.jpg
    ./_Imgs/20231008_102440.jpg

    got only one nail:
    ./_Imgs/20231008_102117.jpg
    ./_Imgs/20231008_102238.jpg

    everything else doesnt seem to work
    

    ------
    #new data set new mask
    COIN_MIN = np.array([9, 5, 0])
    COIN_MAX = np.array([23, 82, 175])
    COINHIGH_MIN = np.array([3, 17, 17])
    COINHIGH_MAX = np.array([25, 126, 75])

    #Nail only mask
    PINK_MIN = np.array([140, 23, 126])
    PINK_MAX = np.array([174, 255, 248])
    NAILWHITE_MIN= np.array([127, 7, 39])
    NAILWHITE_MAX= np.array([170, 25, 199])

    BG_MIN = np.array([0, 0, 141])
    BG_MAX = np.array([143, 255, 255])

    WORKING
    ./_Imgs/20231008_102117.jpg
    ./_Imgs/20231008_102238.jpg #just one nail
    EVERYTHING DOESNT WORK i gave up

    ------
    # #mostly from old data set
    # COIN_MIN = np.array([0, 0, 0])
    # COIN_MAX = np.array([26, 40, 142])
    # COINHIGH_MIN = np.array([13, 1, 25])
    # COINHIGH_MAX = np.array([31, 255, 255])

    # #Nail only mask
    # PINK_MIN = np.array([0, 38, 165])
    # PINK_MAX = np.array([5, 101, 255])
    # NAILWHITE_MIN= np.array([8, 47, 165])
    # NAILWHITE_MAX= np.array([11, 83, 197])

    # BG_MIN = np.array([0, 0, 158])
    # BG_MAX = np.array([179, 39, 247])

    WORKING:
    ./_Images-standard/20231007_160450.jpg
    ./_Images-standard/20231007_160446.jpg - is this not the same image wat
    ./_Images-standard/20231007_160355.jpg
    ./_Images-standard/20231007_155811.jpg - one pathetic nail
    ./_Images/20231007_155732.jpg - one nail only (scuffed with others)
    ./_Images-standard/20231007_144453.jpg - can detect that its a finger not a nail (GOOD)
```
'''

'''
------
    #new data set new mask
    COIN_MIN = np.array([9, 5, 0])
    COIN_MAX = np.array([23, 82, 175])
    COINHIGH_MIN = np.array([3, 17, 17])
    COINHIGH_MAX = np.array([25, 126, 75])

    PINK_MIN = np.array([0, 33, 123])
    PINK_MAX = np.array([7, 139, 255])
    NAILWHITE_MIN = np.array([8, 64, 124])
    NAILWHITE_MAX = np.array([16, 113, 156])

    BG_MIN = np.array([8, 0, 158])
    BG_MAX = np.array([179, 255, 255])

    WORKING kinda:
    ./_Imgs/20231008_102721.jpg
    ./_Imgs/20231008_102543.jpg
    ./_Imgs/20231008_102516.jpg
    ./_Imgs/20231008_102440.jpg

    got only one nail:
    ./_Imgs/20231008_102117.jpg
    ./_Imgs/20231008_102238.jpg

    everything else doesnt seem to work
    

    ------
    #new data set new mask
    COIN_MIN = np.array([9, 5, 0])
    COIN_MAX = np.array([23, 82, 175])
    COINHIGH_MIN = np.array([3, 17, 17])
    COINHIGH_MAX = np.array([25, 126, 75])

    #Nail only mask
    PINK_MIN = np.array([140, 23, 126])
    PINK_MAX = np.array([174, 255, 248])
    NAILWHITE_MIN= np.array([127, 7, 39])
    NAILWHITE_MAX= np.array([170, 25, 199])

    BG_MIN = np.array([0, 0, 141])
    BG_MAX = np.array([143, 255, 255])

    WORKING
    ./_Imgs/20231008_102117.jpg
    ./_Imgs/20231008_102238.jpg #just one nail
    EVERYTHING DOESNT WORK i gave up

    ------
    # #mostly from old data set
    # COIN_MIN = np.array([0, 0, 0])
    # COIN_MAX = np.array([26, 40, 142])
    # COINHIGH_MIN = np.array([13, 1, 25])
    # COINHIGH_MAX = np.array([31, 255, 255])

    # #Nail only mask
    # PINK_MIN = np.array([0, 38, 165])
    # PINK_MAX = np.array([5, 101, 255])
    # NAILWHITE_MIN= np.array([8, 47, 165])
    # NAILWHITE_MAX= np.array([11, 83, 197])

    # BG_MIN = np.array([0, 0, 158])
    # BG_MAX = np.array([179, 39, 247])

    WORKING:
    ./_Images-standard/20231007_160450.jpg
    ./_Images-standard/20231007_160446.jpg - is this not the same image wat
    ./_Images-standard/20231007_160355.jpg
    ./_Images-standard/20231007_155811.jpg - one pathetic nail
    ./_Images/20231007_155732.jpg - one nail only (scuffed with others)
    ./_Images-standard/20231007_144453.jpg - can detect that its a finger not a nail (GOOD)
```
'''