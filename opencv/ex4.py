import cv2
img = cv2.imread("v.jpg")
cv2.imshow("V", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow("Grayscale",gray)
cv2.waitKey(0)