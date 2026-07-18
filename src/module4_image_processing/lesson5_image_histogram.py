"""
==========================================
Module 4 - Image Processing
Lesson 5 - Image Histogram
==========================================
"""

import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display image
cv2.imshow("Grayscale Image", gray)

# Plot Histogram
plt.title("Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.hist(gray.ravel(), bins=256, range=[0, 256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Lesson 5 Completed Successfully!")