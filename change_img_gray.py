import cv2
#读入原始图像，使用cv2.IMREAD_UNCHANGED
img = cv2.imread("D:/Code_VScode/Python_opencv/test.jpg",cv2.IMREAD_UNCHANGED)
#查看打印图像的shape
shape = img.shape
print(shape)
#判断通道是否为3通道或者4通道
if shape[2] == 3 or shape[2] ==4 :
    #将彩色图转化成单通道图
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #通道转化，单通道转为三通道灰度图
    #img_color = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)
    cv2.imshow("gray_image",img_gray)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()