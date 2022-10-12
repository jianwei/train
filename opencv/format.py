#coding:utf-8
import os
import xmltodict
import shutil


def format_img(floder,img_type):
    path_folder = floder+"_source"
    output_file = "negdata.txt" if img_type == -1 else "posdata.txt"
    with open(output_file,'w',encoding='utf-8')as file:
        file.write("")
    for j in range(len(os.listdir(path_folder))):
        i = os.listdir(path_folder)[j]
        file_name = os.path.join(path_folder, i)
        if(file_name.find(".xml")!=-1 and file_name.find(".txt")==-1):
            # print("file_name-1:",file_name)
            points = get_label(file_name)
            new_file_name = str(j+1)+".jpg"
            shutil.copyfile(file_name,floder+"/"+new_file_name)
            points_str =floder+"/"+new_file_name+" "+str(len(points)) +" "
            # print("points_str-1:",points_str)
            for item in points:
                points_str += " ".join(item)
                points_str += "    "
            print("item:",points_str)
            txt=open(output_file,mode='a')
            txt.write(points_str+'\n')
            txt.close()




        

def get_label(file_name):
    with open(file_name) as xml_file:
        parser_data = xmltodict.parse(xml_file.read())   
        xml_file.close()
        object = parser_data["annotation"]["object"]
        ret = []
        if isinstance(object,list):
            for item in object:
                ret.append(get_object_item(item))
        elif(isinstance(object,dict)):
            ret.append(get_object_item(object))
        return ret

def get_object_item(data):
    bndbox = data["bndbox"]
    width = int(bndbox.get("xmax"))-int(bndbox.get("xmin"))
    height = int(bndbox.get("ymax"))-int(bndbox.get("ymin"))
    return (str(bndbox.get("xmin")),str(bndbox.get("ymin")),str(width),str(height))

   
    


if __name__ == '__main__':
    format_img("posdata",1)
    # label = get_label("./posdata/IMG_20221011_094104.xml")
    # print(label)
    pass