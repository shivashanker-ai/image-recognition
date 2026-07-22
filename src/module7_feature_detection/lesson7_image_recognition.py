"""
==========================================
Module 7 - Feature Detection
Lesson 7 - Image Recognition using ORB
==========================================
"""

import cv2

# Load Images
image1 = cv2.imread("dataset/flower.jpg")
image2 = cv2.imread("dataset/flower2.jpg")

# Convert to Grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Create ORB Detector
orb = cv2.ORB_create()

# Detect Keypoints and Descriptors
keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

# Create BF Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match Features
matches = bf.match(descriptors1, descriptors2)

# Sort Matches
matches = sorted(matches, key=lambda x: x.distance)

# Draw Best 30 Matches
matched_image = cv2.drawMatches(
    image1,
    keypoints1,
    image2,
    keypoints2,
    matches[:30],
    None,
    flags=2
)

# Recognition Decision
if len(matches) > 50:
    print("Recognition Result: Same Object Detected")
else:
    print("Recognition Result: Different Objects")

# Display Result
cv2.imshow("Image Recognition using ORB", matched_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Total Matches:", len(matches))
print("Module 7 - Lesson 7 Completed Successfully!")