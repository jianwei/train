import cv2
import os,numpy,shutil


class BatchDoneImage():
    def __init__(self):
        pass
 
    def rename(self,path):
        filelist = os.listdir(path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(path), item)
                dst = os.path.join(os.path.abspath(path), str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except :
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))
    




    "path是图片路径，执行后，会在同一目录下生成11张依次旋转30度的图片"
    def spin(self,folder,rangle=30):
        filelist = os.listdir(folder)  
        for item in filelist:
            path = os.path.join(os.path.abspath(folder), item)
            if(not path.find(".jpg")==-1): 
                retval=cv2.imread(path)
                he,we=retval.shape[:2]
                total = int(360/rangle)
                for x in range(1,total):
                    M=cv2.getRotationMatrix2D(center=(we/2,he/2),angle=x*rangle,scale=1)
                    M=cv2.warpAffine(retval,M,(we,he))
                    new_path=path[:-3]+'-spin'+str(x)+'.jpg'
                    cv2.imwrite(new_path,M)


    

 
    def convertjpg(self,folder,width=40,height=40):
        filelist = os.listdir(folder)  
        for item in filelist:
            path = os.path.join(os.path.abspath(folder), item)
            if(not path.find(".jpg")==-1):
                img = cv2.imread(path)
                resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
                cv2.imwrite(path,resized)
    

    def writetxt(self,folder):
        filelist = os.listdir(folder)  
        for item in filelist:
            path = os.path.join(os.path.abspath(folder), item)
            if os.path.splitext(path)[1] == '.jpg':
                flie_name = "./pos.txt" if not folder.find("pos") == -1 else "neg.txt"
                with open(flie_name,"a") as f:
                    if (not folder.find("pos") == -1):
                        f.write(path+' 1'+' 0'+' 0'+' 40'+' 40'+'\n')
                    else:
                        f.write(path+'\n')
    

    def format(self,folder):
        folder = self.cp(folder)
        self.convertjpg(folder)
        # self.spin(folder,10)
        self.rename(folder)
        self.writetxt(folder)
    
    def cp(self,floder):
        target_dir ="pos_data" if floder.find("pos") !=-1 else "neg_data"
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        shutil.copytree(floder, target_dir)
        return target_dir

    
    "path是图片路径,执行后会在同一目录下生成五张亮度依次递增的图片"
    def light(self,folder):
        pass
        # filelist = os.listdir(folder)  
        # for item in filelist:
        #     path = os.path.join(os.path.abspath(folder), item)
        #     if os.path.splitext(path)[1] == '.jpg':
        #         img=cv2.imread(path)
        #         # print(img.shape)
        #         # cols, rows,channels = img.shape
        #         bright_img = img + Scalar(50,50,50);
        #         bright_img = cv2.convertScaleAbs(img, alpha =0.8, beta = 128)
        #         cv2.imwrite("pos/2.jpg", bright_img)
                # print("retval",retval)
                # img_hsv = cv2.cvtColor(retval, cv2.COLOR_BGR2HSV)
                # darker_hsv = img_hsv.copy()
                # print("darker_hsv",darker_hsv)
                # for y in range(1,6):

                #     darker_hsv[:, :, 2] = darker_hsv[:, :, 2]+2*y
                #     darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
                #     print("darker_img",darker_img)
                #     new_path=path[:-3]+'-light+'+str(y)+'ipg'
                #     print(new_path)
                    # cv2.imwrite(new_path, darker_img)


if __name__ == '__main__':
    print(cv2.__version__)
    demo = BatchDoneImage()
    demo.format("./pos")
    demo.format("./neg")

    
    
    
    pass