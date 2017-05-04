import easygui as g
import sys
import os
def main():
    dir1 = g.diropenbox('请选择您的代码库', '浏览文件夹')
    s1 = set(['.py','.php','.txt','.mp4','.avi'])
    l1 = []
    d1 = {}
    for i in s1:
        l1.append(i[1:])
    for cha in l1:
        d1[cha] = [0,0]
    searchmatchfile(dir1,d1)
    monitor(d1)

def searchmatchfile(dir1,d1):
    os.chdir(dir1)
    for each in os.listdir(os.curdir):
        if os.path.isfile(each):
            tongji(each,d1)
        elif os.path.isdir(each):
            searchmatchfile(each,d1)
            os.chdir(os.pardir)
def tongji(file,d1):
    filetype = os.path.splitext(file)[1][1:]
    if filetype in d1:
        with open(file) as f:
            length = len(f.readlines())
        d1[filetype][0] += 1
        d1[filetype][1] += length

def monitor(d1):
    charnum = 0
    for k,v in d1.items():
        charnum += v[1]
    process = charnum / 100000 % 100
    remian = 100000 - charnum
    msg = '您目前共累计编写了%d行代码，完成进度：%f%%，\n离10万行代码还剩%d行，请继续努力！' % (charnum,process,remian)
    content = []
    for k,v in d1.items():
        content.append('[.' + k + ']' + '源文件' + str(v[0]) + '个，源代码' + str(v[1]) + '行\n')
    g.textbox(msg,'统计结果',text=content)

if __name__ == '__main__':
    main()























