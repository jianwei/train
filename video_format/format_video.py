# coding=utf-8
import os
import cv2
import shutil
import time

EXTRACT_FREQUENCY = 4  # 帧提取频率

def extract_frames(video_path, dst_folder, index):
    # 实例化视频对象
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    t0 = str(time.time())
    # 循环遍历视频中的所有帧
    while True:
        # 逐帧读取
        _, frame = video.read()
        if frame is None:
            break
        # 按照设置的频率保存图片
        if frame_count % EXTRACT_FREQUENCY == 0:
            # 设置保存文件名
            save_path = "{}/{}-{:>03d}.jpg".format(dst_folder,t0,index)
            # 保存图片
            cv2.imwrite(save_path, frame)
            index += 1  # 保存图片数＋1
        frame_count += 1  # 读取视频帧数＋1

    # 视频总帧数˝
    # print(f'the number of frames: {frame_count}')
    # 打印出所提取图片的总数
    print("vide0:{}, image save {:d} imgs".format(video_path,index - 1))
    # 最后释放掉实例化的视频
    video.release()
    return index


def main(video_path):
    video_list = traversal_files(video_path)
    totel_images = 0
    for item in video_list:
        image_path = os.path.join("./images", item)
        video_path = os.path.join("./video", item)
        # build_img_path(image_path)
        # images_number = extract_frames(video_path,image_path,1)
        # print ("video {} done ".format(item))
        # totel_images += images_number
    print("Totally save {} imgs".format(totel_images))




def build_img_path(path):
    try:
        shutil.rmtree(path)
    except OSError:
        pass
    os.mkdir(path)

def traversal_files(path):
    file_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        file_list = files
    return file_list


if __name__ == '__main__':
    main("./video")
