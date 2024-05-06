import cv2
import numpy as np

# Create a black image
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw face outline (circle)
cv2.circle(img, (200, 200), 100, (255, 255, 255), 2)

# Draw eyes (circles)
cv2.circle(img, (170, 170), 10, (255, 255, 255), -1)
cv2.circle(img, (230, 170), 10, (255, 255, 255), -1)

# Draw nose (triangle)
pts = np.array([[200, 190], [185, 220], [215, 220]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (255, 255, 255), 2)

# Draw mouth (rectangle)
cv2.rectangle(img, (180, 240), (220, 250), (255, 255, 255), -1)

# Display the image
cv2.imshow('Human Face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
