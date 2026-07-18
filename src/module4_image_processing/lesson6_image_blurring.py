"""
==========================================
Module 4 - Image Processing
Lesson 6 - Image Blurring
==========================================
"""

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Apply Blur
blur = cv2.blur(image, (7, 7))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lesson 6 Completed Successfully!")