import os
f = open('vedioList.txt','a+')
def search(direc):
    os.chdir(direc)
    for each in os.listdir(os.curdir):
        if os.path.splitext(each)[1] == '.avi' or os.path.splitext(each)[1] == '.rmvb' or os.path.splitext(each)[1] == '.mp4':
            f.write(os.getcwd() + os.sep + each + '\n')
        if os.path.isdir(each):
            search(each)
            os.chdir(os.pardir)

direc = input('DIR：')
search(direc)

