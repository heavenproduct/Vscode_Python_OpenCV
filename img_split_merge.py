import cv2 as cv
import numpy as np
src = cv.imread('D:/Code_VScode/Python_opencv/test.jpg')
#cv.namedWindow('before',cv.WINDOW_NORMAL)
cv.imshow('before',src)
cv.waitKey(0)

#通道分离
b,g,r = cv.split(src)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
cv.waitKey(0)

#通道合并
src = cv.merge([b,g,r])
cv.imshow('merge',src)
cv.waitKey(0)

#修改某个通道
src[:,:,2] = 100
cv.imshow('single',src)
cv.waitKey(0)
cv.destroyAllWindows()