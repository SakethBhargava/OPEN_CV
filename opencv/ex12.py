import cv2
import numpy as np

# Create a black canvas
canvas = np.zeros((600, 600, 3), dtype=np.uint8)

# Draw robot body (rectangle)
cv2.rectangle(canvas, (100, 200), (500, 400), (150, 150, 150), -1)

# Draw robot head (ellipse)
cv2.ellipse(canvas, (300, 150), (80, 60), 0, 0, 360, (200, 200, 200), -1)

# Draw eyes (circles)
cv2.circle(canvas, (270, 135), 10, (0, 0, 255), -1)
cv2.circle(canvas, (330, 135), 10, (0, 0, 255), -1)

# Draw antennas (lines)
cv2.line(canvas, (270, 70), (270, 150), (200, 200, 200), 5)
cv2.line(canvas, (330, 70), (330, 150), (200, 200, 200), 5)

# Draw arms (rectangles)
cv2.rectangle(canvas, (50, 200), (90, 400), (200, 200, 200), -1)
cv2.rectangle(canvas, (510, 200), (550, 400), (200, 200, 200), -1)

# Draw legs (rectangles)
cv2.rectangle(canvas, (200, 400), (250, 550), (200, 200, 200), -1)
cv2.rectangle(canvas, (350, 400), (400, 550), (200, 200, 200), -1)

# Display the image
cv2.imshow('Complex Robot', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()