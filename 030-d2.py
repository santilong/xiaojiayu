import os
<<<<<<< HEAD
def search(dir,file):
    os.chdir(dir)
=======
def search(dirfile,file):
    os.chdir(dirfile)
>>>>>>> 63aeea4d4ec93c10634f1bdfa1381e122615658c
    for each in os.listdir(os.curdir):
        if each == file:
            print(os.getcwd() + os.sep + file)
        if os.path.isdir(each):
<<<<<<< HEAD
            # search(each,file)
            os.chdir(each)
            if os.path.exists(file):
                print(os.getcwd() + os.sep + file)
            os.chdir(os.pardir)
dir = input('请输入待查找的初始目录：')
file = input('请输入需要查找的目标文件：')
search(dir,file)
=======
            search(each,file)
            os.chdir((os.pardir)
dirfile = input('请输入待查找的初始目录：')
file = input('请输入需要查找的目标文件：')
search(dirfile,file)




>>>>>>> 63aeea4d4ec93c10634f1bdfa1381e122615658c
