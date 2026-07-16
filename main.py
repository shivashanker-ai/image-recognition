import cv2

# Read the image
image = cv2.imread("dataset/flower.jpg")

if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    print("Original Shape:", image.shape)
    print("Grayscale Shape:", gray.shape)

    # Display both images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()