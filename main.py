import cv2
import  numpy as np

img = np.ones((300,300,3),np.uint8)*255
cv2.imshow("img",img)
cv2.waitKey(0)