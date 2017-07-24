#Thresholding helps convert to white or black, so helps to further simplify
#Preferable to first convert color image to gray scale (which has 255 values) & then threshold operation is done
#Threshold types - Binary, Gaussian, Otsu threshold. Adaptive threshold

import numpy as np
import cv2

img = cv2.imread('D:\\SentDex\\images\\bookpage.jpg')
print img.shape
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval2, otsu = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('color_binary', threshold)
cv2.imshow('gray_binary', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()


