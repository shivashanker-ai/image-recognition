"""
==========================================
Module 7 - Feature Detection
Lesson 4 - FAST Feature Detector
==========================================
"""

import cv2

# Load Image
image = cv2.imread("dataset/flower.jpg")

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create FAST Detector
fast = cv2.FastFeatureDetector_create()

# Detect Keypoints
keypoints = fast.detect(gray_image, None)

# Draw Keypoints
output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    color=(0, 0, 255)
)

# Display Image
cv2.imshow("FAST Feature Detection", output)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Module 7 - Lesson 4 Completed Successfully!")