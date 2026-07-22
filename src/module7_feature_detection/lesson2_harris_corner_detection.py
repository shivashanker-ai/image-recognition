"""
==========================================
Module 7 - Feature Detection
Lesson 2 - Harris Corner Detection
==========================================
"""

import cv2
import numpy as np

# Load Image
image = cv2.imread("dataset/flower.jpg")

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert image to float32
gray_image = np.float32(gray_image)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray_image, 2, 3, 0.04)

# Dilate corner points
corners = cv2.dilate(corners, None)

# Mark detected corners in Red
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display Images
cv2.imshow("Harris Corner Detection", image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 7 - Lesson 2 Completed Successfully!")