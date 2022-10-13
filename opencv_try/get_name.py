import os

# 遍历文件夹

def walkFile(input,output):
    with open(output,'a+',encoding='utf-8')as file:
        file.write("")

    for root, dirs, files in os.walk(input):
        for f in files:
            print(f)
            with open(output,'a+',encoding='utf-8')as file:
                file.write(f+"\n")



if __name__ == '__main__':
    # floder1 = "./posdata"
    # floder2 = "./negdata"
    walkFile('./posdata','posdata.txt')
    walkFile('./negdata','negdata.txt')