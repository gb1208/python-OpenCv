import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\SentDex\images\logo.png', 1)
b,g,r = cv2.split(img)

#img2 = cv2.merge([r,g,b])
#img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img2 = img[:,:,::-1]

plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img2)

plt.show()

cv2.imshow('bgr image', img)
cv2.imshow('rgb image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()