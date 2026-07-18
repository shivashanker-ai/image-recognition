"""
==========================================
Module 4 - Image Processing
Lesson 2 - Image Filtering
==========================================

"""

import cv2

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Apply Average Blur
average = cv2.blur(image, (7, 7))

# Apply Gaussian Blur
gaussian = cv2.GaussianBlur(image, (7, 7), 0)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Average Blur", average)
cv2.imshow("Gaussian Blur", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lesson 2 Completed Successfully!")