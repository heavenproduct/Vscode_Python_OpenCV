import cv2
import os
os.chdir('D:/Code_VScode/Python_opencv/')

def process(image):
	#面积阈值
    min_area=100
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv = cv2.medianBlur(hsv, 5)
    mask = cv2.inRange(hsv, (11, 43, 46), (25, 255, 255))
    line = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5), (-1, -1))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, line)
    cv2.imshow("mask",mask)


    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for c in range(len(contours)):
        area = cv2.contourArea(contours[c])
        if area > min_area:
        # 绘制
            x, y, w, h = cv2.boundingRect(contours[c])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image,"orange",(x, y), font, 1.2, (0, 0, 255), 2)
    return image


image=cv2.imread("orange.jpg")
result = process(image)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
