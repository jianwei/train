#coding:utf-8
import cv2 as cv
import time
 
# 识别电脑摄像头并打开
cap = cv.VideoCapture(2)

# 调用熟悉的人脸分类器 识别特征类型
# 人脸 - haarcascade_frontalface_default.xml
# 人眼 - haarcascade_eye.xm
# 微笑 - haarcascade_smile.xml
face_detect = cv.CascadeClassifier('./xml2/cascade.xml')

while True:
    t1 = time.time()
    # 读取视频片段
    flag, frame = cap.read()
    if flag == False:
        break

    # 灰度处理
    gray = cv.cvtColor(frame, code=cv.COLOR_BGR2GRAY)

    # 检查人脸 按照1.1倍放到 周围最小像素为5
    face_zone = face_detect.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
    print("face_zone:",face_zone)
    # 绘制矩形和圆形检测人脸
    for x, y, w, h in face_zone:
        cv.rectangle(frame, pt1 = (x, y), pt2 = (x+w, y+h), color = [0,0,255], thickness=2)
        cv.circle(frame, center = (x + w//2, y + h//2), radius = w//2, color = [0,255,0], thickness = 2)

    t2 = time.time()
    fps = round(1 /(t2-t1),3)
    cv.putText(frame,"fps:{}".format(round(fps,3)), (0,30),0,1,(0, 0, 255),thickness=2,lineType=cv.LINE_AA)
    # 显示图片
    cv.imshow('video', frame)

    # 设置退出键和展示频率
    if ord('q') == cv.waitKey(40):
        break
 
# 释放资源
cv.destroyAllWindows()
cap.release()