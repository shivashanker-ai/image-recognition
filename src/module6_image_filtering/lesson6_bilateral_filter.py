"""
==========================================
Module 6 - Image Filtering
Lesson 6 - Bilateral Filter
==========================================
"""

import cv2

# Load the image
image = cv2.imread("dataset/flower.jpg")

# Apply Bilateral Filter
bilateral_image = cv2.bilateralFilter(image, 9, 75, 75)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Bilateral Filter", bilateral_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 6 - Lesson 6 Completed Successfully!")