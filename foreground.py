#grabcut foreground extraction
#For examples - 1. https://github.com/opencv/opencv/blob/master/samples/python/grabcut.py
#2. http://docs.opencv.org/3.2.0/d8/d83/tutorial_py_grabcut.html
#3. http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html


import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:\\SentDex\\images\\kinsley.jpg')
print img.shape
print img.shape[:2]
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

#rect = (161, 79, 150, 150)
rect = (50, 50, 300, 500)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
img = img*mask2[:,:, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()