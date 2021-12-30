import cv2
import numpy as np

img = cv2.imread("/home/hritik/workspace/nibbapy/antic.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)


cv2.imshow("G",imgGray)
cv2.imshow("b",imgBlur)
cv2.imshow("c",imgCanny)
cv2.imshow("d",imgDilation)
cv2.imshow("e",imgEroded)
cv2.waitKey(0)