#coding:utf-8
import cv2 as cv
import numpy as np
import time,os

def deldir(dir):
    if not os.path.exists(dir):
        return False
    if os.path.isfile(dir):
        os.remove(dir)
        return
    for i in os.listdir(dir):
        t = os.path.join(dir, i)
        if os.path.isdir(t):
            deldir(t)#重新调用次方法
        else:
            os.unlink(t)


def format_video(video_name,output): 
    deldir(output)
    output_file = "{}.txt".format(output)
    with open(output_file,'w',encoding='utf-8')as file:
        file.write("")
    # 加载视频
    cap = cv.VideoCapture(video_name)
    while True:
        t1 = time.time()
        flag, frame = cap.read()
        if flag == False:
            break
        t2 = time.time()
        file_name = "./{}/{}.jpg".format(output,str(t2))
        cv.imwrite(file_name,frame)
        with open(output_file,'a+',encoding='utf-8')as file:
                file.write(str(t2)+".jpg\n")

        print("file_name:{},fps:{}".format(file_name,1/(t2-t1)))
    # 释放资源
    cv.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    format_video("13_1664891248.mp4",'negdata')
    format_video("12_1664890899.mp4",'posdata')
    pass