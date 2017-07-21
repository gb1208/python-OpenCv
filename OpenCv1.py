import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('D:\SentDex\images\logo.png', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image', img)
#k = cv2.waitKey(0) & 0xFF
#if k == 27:
#    cv2.destroyAllWindows()
#elif k == ord('s'):
#    cv2.imwrite('D:\SentDex\images\testimg.png', img)
#    cv2.destroyAllWindows()

#matplotlib section
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

