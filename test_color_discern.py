import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    #获取每一帧
    ret, frame = cap.read()
    
    #准换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #设定阈值
    lower_red = np.array([0, 127, 128])  # 红色阈值下界 
    upper_red = np.array([10, 255, 255])  # 红色阈值上界
    lower_green = np.array([35, 110, 106])  # 绿色阈值下界
    upper_green = np.array([77, 255, 255])  # 绿色阈值上界 
    lower_blue = np.array([110,50,50])  # 蓝色阈值下界 
    upper_blue = np.array([130,255,255]) # 蓝色阈值上界 
    
    #根据阈值构建掩模
    mask_red = cv2.inRange(hsv,lower_red,upper_red)
    mask_green = cv2.inRange(hsv,lower_green,upper_green)
    mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
    
    #对原图像和掩模进行位运算
    res_red = cv2.bitwise_and(frame,frame,mask=mask_red)
    res_green = cv2.bitwise_and(frame,frame,mask=mask_green)
    res_blue = cv2.bitwise_and(frame,frame,mask=mask_blue)
    
    #显示图像
    cv2.imshow('frame',frame)
    #检测红色
    cv2.imshow('mask',mask_red)
    cv2.imshow('res',res_red)
    #检测绿色
    #cv2.imshow('mask',mask_green)
    #cv2.imshow('res',res_green)
    #检测蓝色
    #cv2.imshow('mask',mask_blue)
    #cv2.imshow('res',res_blue)
    
    k = cv2.waitKey(5)&0xFF
    if k == 27:
        break
#关闭窗口
cv2.destroyAllWindows()
     