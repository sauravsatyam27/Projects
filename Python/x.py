import cv2
print(cv2.__version__)
cv2.imshow("test", cv2.imread("some_image.jpg"))
cv2.waitKey(0)
