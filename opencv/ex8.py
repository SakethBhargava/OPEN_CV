import cv2
import numpy as np
img = cv2.imread("Kushi.jpg")
cv2.imshow("Kushi.jpg",img)
height=img.shape[0]
width=img.shape[1]
print("Img Dimensions :",height,width)
M = np.float32([[1,0,100],[0,1,50]])
img2 = cv2.warpAffine(img,M,(width,height))
cv2.imshow('Image Translation', img2)
sacle = 200
w = int(img.shape[1] * sacle / 100)
h = int(img.shape[0] * sacle / 100)
dim=(w,h)
scaled_img=cv2.resize(img,dim)
cv2.imshow("Scaled Image",scaled_img)
cv2.waitKey(0)