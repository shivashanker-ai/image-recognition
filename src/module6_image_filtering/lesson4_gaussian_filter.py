"""
==========================================
Module 6 - Image Filtering
Lesson 4 - Gaussian Filter
==========================================
"""

import cv2

# Load the image
image = cv2.imread("dataset/flower.jpg")

# Apply Gaussian Blur
gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blur", gaussian_image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 6 - Lesson 4 Completed Successfully!")