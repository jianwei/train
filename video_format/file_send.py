import os,shutil

def train_data(from_path,target_path):
    num = 0
    for root, dirs, files in os.walk(from_path, topdown=False):
        for file in files : 
            split_file = file.split(".")
            if(len(split_file)>2):
                extends = split_file[2]
                if(extends=="jpg"):
                    file_name = split_file[0]+"."+split_file[1]
                    is_exists = check_exists(file_name,files)
                    if is_exists:
                        image_file_path = os.path.join(root,file)
                        txt_file_path = os.path.join(root,file_name+".txt")
                        image_to_path = target_path+"/train/images"
                        labels_to_path = target_path+"/train/labels"
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
            if(len(split_file)>2):
                extends = split_file[2]
                if(extends=="jpg"):
                    file_name = split_file[0]+"."+split_file[1]
                    is_exists = check_exists(file_name,files)
                    if is_exists:
                        if (num%5==0):
                            image_file_path = os.path.join(root,file)
                            txt_file_path = os.path.join(root,file_name+".txt")
                            image_to_path = target_path+"/valid/images"
                            labels_to_path = target_path+"/valid/labels"
                            shutil.copy(image_file_path, image_to_path)
                            shutil.copy(txt_file_path, labels_to_path)
                            valid_num +=1
                        num+=1
    print("valid_num images num:",valid_num)


    pass


def main(from_path,target_path):
    train_data(from_path,target_path)
    valid_data(from_path,target_path)
    

def check_exists(file_name,files):
    txt = file_name+".txt"
    ret = False
    for item in files:
        # print(item)
        if (txt==item):
            ret = True
    return ret





if __name__ == '__main__':
    main("./images","../chives_data")