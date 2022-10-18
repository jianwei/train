#coding:utf-8
import cv2 
import time
    
# 识别电脑摄像头并打开
cap = cv2.VideoCapture(2)

# 调用熟悉的人脸分类器 识别特征类型
# 人脸 - haarcascade_frontalface_default.xml
# 人眼 - haarcascade_eye.xm
# 微笑 - haarcascade_smile.xml
face_detect = cv2.CascadeClassifier('./xml2/cascade.xml')

while True:
    t1 = time.time()
    # 读取视频片段
    flag, frame = cap.read()

    # reading image
    # image = cv2.imread('img002.jpg')

    # convert the image to grayscale format
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply binary thresholding
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

    # visualize the binary image
    # cv2.imshow('Binary image', thresh)

    # collectiong contours
    contours,h = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # looping through contours
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,215,255),2)

    # if flag == False:
    #     break

    # # 灰度处理
    # gray = cv.cvtColor(frame, code=cv.COLOR_BGR2GRAY)

    # # 检查人脸 按照1.1倍放到 周围最小像素为5
    # face_zone = face_detect.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
    # print("face_zone:",face_zone)
    # # 绘制矩形和圆形检测人脸
    # for x, y, w, h in face_zone:
    #     cv.rectangle(frame, pt1 = (x, y), pt2 = (x+w, y+h), color = [0,0,255], thickness=2)
    #     cv.circle(frame, center = (x + w//2, y + h//2), radius = w//2, color = [0,255,0], thickness = 2)

    t2 = time.time()
    fps = round(1 /(t2-t1),3)
    cv2.putText(frame,"fps:{}".format(round(fps,3)), (0,30),0,1,(0, 0, 255),thickness=2,lineType=cv2.LINE_AA)
    # 显示图片
    cv2.imshow('video', frame)

    # 设置退出键和展示频率
    if ord('q') == cv2.waitKey(40):
        break
        
# 释放资源
cv2.destroyAllWindows()
cap.release()