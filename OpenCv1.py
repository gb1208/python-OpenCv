import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('D:\SentDex\images\logo.png', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

