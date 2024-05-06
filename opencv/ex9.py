import cv2
import numpy as np

# Create a black image
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a circle
cv2.circle(img, (200, 200), 50, (25, 0, 255), -1)

# Draw a rectangle
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 2)

# Draw a triangle
pts = np.array([[300, 50], [250, 150], [350, 150]], np.int32)
cv2.polylines(img, [pts], True, (255, 0, 0), 2)

# Draw a square
cv2.rectangle(img, (250, 200), (350, 350), (255, 255, 0), -1)

# Display the image
cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
