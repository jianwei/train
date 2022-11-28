import os,shutil

def train_data(from_path,target_path):
    num = 0
    for root, dirs, files in os.walk(from_path, topdown=False):
        for file in files : 
            split_file = file.split(".")
            if(len(split_file)==2):
                extends = split_file[1]
                if(extends=="jpg"):
                    file_name = split_file[0]
                    is_exists = check_exists(file_name,files)
                    if is_exists:
                        image_file_path = os.path.join(root,file)
                        txt_file_path = os.path.join(root,file_name+".xml.txt")
                        image_to_path = target_path+"/train/images"
                        folder_exists(image_to_path)
                        labels_to_path = target_path+"/train/labels/"
                        folder_exists(labels_to_path)
                        print("image_to_path,labels_to_path:",image_to_path,labels_to_path)
                        shutil.copy(image_file_path, image_to_path)
                        shutil.copy(txt_file_path, labels_to_path)
                        num+=1
    print("train_data images num:",num)
    pass


def valid_data(from_path,target_path):
    num = 0
    valid_num = 0
    for root, dirs, files in os.walk(from_path, topdown=False):
        for file in files : 
            split_file = file.split(".")
            if(len(split_file)==2):
                extends = split_file[1]
                if(extends=="jpg"):
                    file_name = split_file[0]
                    is_exists = check_exists(file_name,files)
                    if is_exists:
                        if (num%5==0):
                            image_file_path = os.path.join(root,file)
                            txt_file_path = os.path.join(root,file_name+".xml.txt")
                            image_to_path = target_path+"/valid/images"
                            folder_exists(image_to_path)
                            labels_to_path = target_path+"/valid/labels"
                            folder_exists(labels_to_path)
                            # labels_to_path = target_path+"/train/labels/"+os.path.join(root,file_name+".txt")
                            shutil.copy(image_file_path, image_to_path)
                            shutil.copy(txt_file_path, labels_to_path)
                            valid_num +=1
                        num+=1
    print("valid_num images num:",valid_num)
    pass

def folder_exists(path):
    if (not os.path.exists(path)):
        os.mkdir(path)
    pass


def rename(from_path):
    for root, dirs, files in os.walk(from_path, topdown=False):
        for file in files:
            file_arr = file.split(".")
            file_end = file_arr[len(file_arr)-1]
            file_path = os.path.join(root,file)
            new_file_name = ""
            if (file_end == "txt"):
                new_file_name = file_arr[0]+".txt"
                new_file_path = os.path.join(root,new_file_name)
                print("file_path:{},new_file_name:{}".format(file_path,new_file_path))
                os.rename(file_path,new_file_path)            
        pass

def main(from_path,target_path):
    clean_data(target_path)
    train_data(from_path,target_path)
    valid_data(from_path,target_path)
    rename(target_path)

def clean_data(target_path):
    if (os.path.exists(target_path+"/train/images")):
        shutil.rmtree( target_path+"/train/images" ) 
    if (os.path.exists(target_path+"/train/labels")):
        shutil.rmtree( target_path+"/train/labels" ) 
    if (os.path.exists(target_path+"/valid/images")):
        shutil.rmtree( target_path+"/valid/images" ) 
    if (os.path.exists(target_path+"/valid/labels")):
        shutil.rmtree( target_path+"/valid/labels" ) 
    pass

def check_exists(file_name,files):
    txt = file_name+".xml.txt"
    ret = False
    for item in files:
        # print(item)
        if (txt==item):
            ret = True
    return ret





if __name__ == '__main__':

    main("/Users/carlos/Desktop/IMG_20221128_111053","./corn_data")
    # rename("../corn_data/")