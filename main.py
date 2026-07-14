import numpy as np

image = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Original Image:")
print(image)

# Horizontal Flip
horizontal = np.fliplr(image)

print("\nHorizontal Flip:")
print(horizontal)

# Vertical Flip
vertical = np.flipud(image)

print("\nVertical Flip:")
print(vertical)

# Rotate 90 Degrees
rotated = np.rot90(image)

print("\nRotate 90°:")
print(rotated)