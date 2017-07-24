import cv2
import numpy as np

#img1 = cv2.imread('D:\SentDex\images\3D-Matplotlib.png')
img3 = cv2.imread('D:\SentDex\images\mainsvmimage.png')
#img2 = cv2.imread('D:\SentDex\images\logo.png')
img4 = cv2.imread('D:\SentDex\images\mainlogo.png')

#part 1............
#print img3.shape
#add = img2 + img3 ##adds the pixel values, max limit for each pixel is 255
##add = cv2.add(img2,img3)
#weighted = cv2.addWeighted(img3, 0.6, img2, 0.4, 0)
#cv2.imshow('add', add)
#cv2.imshow('weighted', weighted)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#part 2............
rows,cols,channels = img4.shape
roi = img3[0:rows, 0:cols]
img2gray = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) #bitwise_or 
img2_fg = cv2.bitwise_and(img4, img4, mask=mask)
dst = cv2.add(img1_bg, img2_fg)
img3[0:rows, 0:cols] = dst
#cv2.imshow('mask',mask)
#cv2.imshow('res', img3)
#cv2.imshow('mask_inv', mask_inv)
#cv2.imshow('img1_bg', img1_bg)
#cv2.imshow('img2_fg', img2_fg)
#cv2.imshow('dest', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()