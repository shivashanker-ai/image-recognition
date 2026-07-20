"""
==========================================
Module 6 - Image Filtering
Lesson 5 - Median Filter
==========================================
"""

import cv2

# Load the image
image = cv2.imread("dataset/flower.jpg")

# Apply Median Filter
median_image = cv2.medianBlur(image, 5)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Median Filter", median_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 6 - Lesson 5 Completed Successfully!")