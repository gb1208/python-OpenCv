import numpy as np
import cv2

#ideally, pick up a colour image, convert to gray, perform analysis and then re-convert to colour
img = cv2.imread('D:\SentDex\images\logo.png', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]

#trying to get colour value of the pixel at postition [55,55]
px = img[55,55]
print (px)

img[100:150, 100:150] = [255,255,255]
roi = img[100:150, 100:150]

watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print roi