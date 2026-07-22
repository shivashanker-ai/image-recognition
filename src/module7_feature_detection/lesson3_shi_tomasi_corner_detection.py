"""
==========================================
Module 7 - Feature Detection
Lesson 3 - Shi-Tomasi Corner Detection
==========================================
"""

import cv2
import numpy as np

# Load Image
image = cv2.imread("dataset/flower.jpg")

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Corners
corners = cv2.goodFeaturesToTrack(
    gray_image,
    maxCorners=100,
    qualityLevel=0.01,
    minDistance=10
)

# Convert Corner Coordinates to Integer
corners = np.int32(corners)

# Draw Corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

# Display Image
cv2.imshow("Shi-Tomasi Corner Detection", image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 7 - Lesson 3 Completed Successfully!")