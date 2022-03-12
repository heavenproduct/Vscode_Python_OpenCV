import cv2
import numpy as np

# 创建一张黑色的背景图
img=np.zeros((512,512,3), np.uint8)

# 绘制一条线宽为5的线段
cv2.line(img,(0,0),(511,511),(255,0,0),1)

# 画一个绿色边框的矩形，参数2：左上角坐标，参数3：右下角坐标
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# 画一个填充红色的圆，参数2：圆心坐标，参数3：半径
cv2.circle(img,(447,63), 63, (0,0,255), -1)

# 在图中心画一个填充的半圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

#绘制多边形
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts], True, (0,0,255),1)

# 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
#添加文字
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)


winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyWindow(winname)
