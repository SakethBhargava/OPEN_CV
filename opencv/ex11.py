import cv2
import numpy as np
image = cv2.imread('kushi.jpg', cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
