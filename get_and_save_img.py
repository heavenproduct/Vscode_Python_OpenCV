#导入opencv的python版本依赖库cv2
import cv2

#使用opencv中imread函数读取图片，
#0代表灰度图形式打开，1代表彩色形式打开
img = cv2.imread('D:/Code_VScode/Python_opencv/test.jpg',-1)
print(img.shape)
#print(img)
cv2.imshow('photo',img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('split_.jpg',img)
    
cv2.destroyAllWindows()