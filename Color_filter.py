import numpy as np
import cv2

# if using a video stream -
#cap = cv2.VideoCapture(0)

# if using an image -
cap = cv2.imread('D:\\SentDex\\images\\red.png')
print cap.shape

while (1):
    #_, frame = cap.read() ## if using a video stream

    #hsv - hue saturation & value
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(cap, cap, mask = mask)

    #for smoothing the image & removing background noise
    #smoothing - a sort of averaging per block of pixels
    kernel = np.ones((15,15), np.float32)/225
    smooth = cv2.filter2D(res, -1, kernel)

    #to improve clarity - Gaussian, Median, bilateral blur.
    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    #cv2.imshow('cap', cap)
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res)
    cv2.imshow('smooth', smooth)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    #k = cv2.waitKey(5) & 0xFF
    #if k == 27:
    #    break

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cap.release() ## if using a video stream