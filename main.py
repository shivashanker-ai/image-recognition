import cv2

image = cv2.imread("dataset/flower.jpg")

cv2.imshow("original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()