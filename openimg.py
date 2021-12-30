import cv2
print("ulla la la ")

img = cv2.imread("/home/hritik/workspace/nibbapy/antic.png")
print(img)
cv2.imshow("Output", img)
cv2.waitKey(0)