import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # capture frame by frame 
    ret,frame = cap.read()
    
    #Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Display the resulting frame 
    cv2.imshow('frame_gray',gray)
    cv2.imshow('frame_color',frame)
    input=cv2.waitKey(20)
    if input == 27 :#or 'q':#如过输入的是q或者esc就break，结束图像显示，鼠标点击视频画面输入字符
        break
#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()