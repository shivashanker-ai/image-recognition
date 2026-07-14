"""
==========================================
Module 1 - Image Fundamentals
Lesson 1 - Pixels
==========================================
"""

# A pixel is the smallest unit of an image.
# A grayscale pixel stores one value between 0 and 255.

pixel = 150

print("Pixel Value:", pixel)

if pixel == 0:
    print("Color: Black")
elif pixel == 255:
    print("Color: White")
else:
    print("Color: Gray Shade")

print("\nMore Pixel Examples")

pixels = [0, 64, 128, 192, 255]

for p in pixels:
    print(f"Pixel Value: {p}")

print("\nA grayscale pixel stores only ONE number.")