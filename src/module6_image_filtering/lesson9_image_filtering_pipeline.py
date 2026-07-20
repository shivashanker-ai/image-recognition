"""
==========================================
Module 6 - Image Filtering
Lesson 9 - Complete Image Filtering Pipeline
==========================================
"""

import cv2

# Load the image
image = cv2.imread("dataset/flower.jpg")

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
gaussian_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Median Filter
median_image = cv2.medianBlur(gaussian_image, 5)

# Apply Canny Edge Detection
canny_edges = cv2.Canny(median_image, 100, 200)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Gaussian Blur", gaussian_image)
cv2.imshow("Median Filter", median_image)
cv2.imshow("Canny Edge Detection", canny_edges)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 6 - Lesson 9 Completed Successfully!")