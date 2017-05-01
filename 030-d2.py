import os
def search(dir,file):
    os.chdir(dir)
    for each in os.listdir(os.curdir):
        if each == file:
            print(os.getcwd() + os.sep + file)
        if os.path.isdir(each):
            # search(each,file)
            os.chdir(each)
            if os.path.exists(file):
                print(os.getcwd() + os.sep + file)
            os.chdir(os.pardir)
dir = input('请输入待查找的初始目录：')
file = input('请输入需要查找的目标文件：')
search(dir,file)
