import cv2
img = cv2.imread("v.jpg")
cv2.imwrite("v.png", img)
cv2.imwrite("v.tiff", img)
cv2.imshow("v.jpg", img)
cv2.imshow("v.png", img)
cv2.imshow("v.tiff", img)
cv2.waitKey(0)