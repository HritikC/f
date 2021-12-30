import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),4)

cv2.rectangle(img,(0,0),(200,300),(0,0,255),2 )

cv2.circle(img,(400,50),30,(255,255,0),5)

cv2.putText(img,"Hritik ", (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,200,300),3)

cv2.imshow("Image",img)
cv2.waitKey(0) 

