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

    #erosion - dilation
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    cv2.imshow('cap', cap)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    #opening - closing
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('cap', cap)
    cv2.imshow('res', res)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    #k = cv2.waitKey(5) & 0xFF
    #if k == 27:
    #    break

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cap.release() ## if using a video stream