"""
==========================================
Module 4 - Image Processing
Lesson 4 - Adaptive Thresholding
==========================================
"""

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Global Threshold
_, global_thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Adaptive Threshold
adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Global Threshold", global_thresh)
cv2.imshow("Adaptive Threshold", adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lesson 4 Completed Successfully!")