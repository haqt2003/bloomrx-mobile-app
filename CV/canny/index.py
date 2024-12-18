# import cv2
# import numpy as np

# img = cv2.imread('download.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

# #canny
# img_canny = cv2.Canny(img,100,200)

# #sobel
# img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
# img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
# img_sobel = img_sobelx + img_sobely


# #prewitt
# kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
# kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
# img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
# img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)


# cv2.imshow("Original Image", img)
# cv2.imshow("Canny", img_canny)
# # cv2.imshow("Sobel X", img_sobelx)
# # cv2.imshow("Sobel Y", img_sobely)
# cv2.imshow("Sobel", img_sobel)
# # cv2.imshow("Prewitt X", img_prewittx)
# # cv2.imshow("Prewitt Y", img_prewitty)
# cv2.imshow("Prewitt", img_prewittx + img_prewitty)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2 
import numpy as np 
  
# Reading the input image 
img = cv2.imread('download.jpg', 0) 
  
# Taking a matrix of size 5 as the kernel 
kernel = np.ones((5, 5), np.uint8) 
  
# The first parameter is the original image, 
# kernel is the matrix with which image is 
# convolved and third parameter is the number 
# of iterations, which will determine how much 
# you want to erode/dilate a given image. 
img_erosion = cv2.erode(img, kernel, iterations=1) 
img_dilation = cv2.dilate(img, kernel, iterations=1) 
  
cv2.imshow('Input', img) 
cv2.imshow('Erosion', img_erosion) 
cv2.imshow('Dilation', img_dilation) 
  