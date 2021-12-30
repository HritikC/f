import cv2
import numpy as np

img = cv2.imread("/home/hritik/workspace/nibbapy/watch.jpeg")
print(img.shape)

imgResize = cv2.resize(img,(600,400))
print(imgResize.shape)

imgCropped = img[0:50,50:100]

cv2.imshow("Image",img)
cv2.imshow("image resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)