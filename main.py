import cv2
import numpy as np

image=cv2.imread("dataset/flower.jpg")

gray_image=cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(
    gray_image,
    maxcorners=100,
    qualityLevel=0.01,
    minDistance=10
)

corners=np.int32(corners)

for corner in corners:
    x,y = corner.revel()
    cv2.circle( image,(x,y),5,(0,0,255), -1)

    cv2.imshow("shi- Tomasi corner Detection", image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()