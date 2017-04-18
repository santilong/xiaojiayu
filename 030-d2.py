import os
def search(dirfile,file):
    os.chdir(dirfile)
    for each in os.listdir(os.curdir):
        if each == file:
            print(os.getcwd() + os.sep + file)
        if os.path.isdir(each):
            search(each,file)
            os.chdir((os.pardir)
dirfile = input('请输入待查找的初始目录：')
file = input('请输入需要查找的目标文件：')
search(dirfile,file)




