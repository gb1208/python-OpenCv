#template matching -
#additional resource - http://docs.opencv.org/3.0-rc1/d4/dc6/tutorial_py_template_matching.html

import numpy as np
import cv2

img_rgb = cv2.imread('D:\\SentDex\\images\\big.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('D:\\SentDex\\images\\small.jpg', 0)
w,h = template.shape[::-1]

#considering all the template matching parameters
#methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]

#for method in methods:
#    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
#    threshold = 0.70
#    loc = np.where (result >= threshold)
#    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

#    for pt in zip(*loc[::-1]):
#        cv2.rectangle(img_rgb, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

#    cv2.imshow('detected', img_rgb)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()


result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.70
loc = np.where (result >= threshold)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

print (minVal)
print (maxVal)
print (minLoc)
print (maxLoc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

cv2.imshow('detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()