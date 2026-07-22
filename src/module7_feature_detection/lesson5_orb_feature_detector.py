"""
==========================================
Module 7 - Feature Detection
Lesson 5 - ORB Feature Detector
==========================================
"""

import cv2

# Load Image
image = cv2.imread("dataset/flower.jpg")

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create ORB Detector
orb = cv2.ORB_create()

# Detect Keypoints and Compute Descriptors
keypoints, descriptors = orb.detectAndCompute(gray_image, None)

# Draw Keypoints
output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    color=(0, 0, 255),
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Display Image
cv2.imshow("ORB Feature Detection", output)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print("Number of Keypoints Detected:", len(keypoints))
print("Descriptor Shape:", descriptors.shape)

print("\nModule 7 - Lesson 5 Completed Successfully!")