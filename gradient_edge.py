import numpy as np
import cv2

# if using a video stream -
#cap = cv2.VideoCapture(0)

# if using an image -
cap = cv2.imread('D:\\SentDex\\images\\red.png')
print cap.shape

while (1):
    #_, frame = cap.read() ## if using a video stream

    #gradient
    laplacian = cv2.Laplacian(cap, cv2.CV_64F)
    sobelx = cv2.Sobel(cap, cv2.CV_64F, 1, 0, ksize = 5)
    sobely = cv2.Sobel(cap, cv2.CV_64F, 0, 1, ksize = 5)
    cv2.imshow('original', cap)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)

    #edge detection
    #edges = cv2.Canny(cap, 100, 200)
    edges = cv2.Canny(cap, 50, 50) #smaller the no. greater the edge info
    cv2.imshow('edges', edges)

    #k = cv2.waitKey(5) & 0xFF
    #if k == 27:
    #    break

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cap.release() ## if using a video stream