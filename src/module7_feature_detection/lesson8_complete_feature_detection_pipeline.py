"""
==========================================
Module 7 - Feature Detection
Lesson 8 - Complete Feature Detection Pipeline
==========================================
"""

import cv2

# -----------------------------------------
# Load Images
# -----------------------------------------

image1 = cv2.imread("dataset/flower.jpg")
image2 = cv2.imread("dataset/flower2.jpg")

# -----------------------------------------
# Convert Images to Grayscale
# -----------------------------------------

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# -----------------------------------------
# Create ORB Detector
# -----------------------------------------

orb = cv2.ORB_create()

# -----------------------------------------
# Detect Keypoints and Compute Descriptors
# -----------------------------------------

keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

# -----------------------------------------
# Create Brute Force Matcher
# -----------------------------------------

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# -----------------------------------------
# Match Features
# -----------------------------------------

matches = bf.match(descriptors1, descriptors2)

# -----------------------------------------
# Sort Matches
# -----------------------------------------

matches = sorted(matches, key=lambda x: x.distance)

# -----------------------------------------
# Recognition Decision
# -----------------------------------------

if len(matches) > 50:
    result = "Same Object Detected"
else:
    result = "Different Objects"

# -----------------------------------------
# Draw Matches
# -----------------------------------------

output = cv2.drawMatches(
    image1,
    keypoints1,
    image2,
    keypoints2,
    matches[:30],
    None,
    flags=2
)

# -----------------------------------------
# Display Results
# -----------------------------------------

cv2.imshow("Feature Detection Pipeline", output)

print("=" * 45)
print("Feature Detection Pipeline")
print("=" * 45)

print("Image 1 Keypoints :", len(keypoints1))
print("Image 2 Keypoints :", len(keypoints2))
print("Total Matches     :", len(matches))
print("Recognition Result:", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nModule 7 - Lesson 8 Completed Successfully!")