import numpy as np
import cv2 as cv
 
img = cv.imread('goc.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# Resize 
height, width = 500, 500
res = cv.resize(img,(width,height), interpolation = cv.INTER_CUBIC)
cv.imwrite('resized_goc4.jpg', res)


# Translate
# rows, cols, _ = img.shape
# M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),75,1)
# dst = cv.warpAffine(img,M,(cols,rows))
# cv.imwrite('resized_goc3.jpg', dst)
