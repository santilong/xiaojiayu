import os
def search(key,yup):
    if yup == 'yes' or yup == 'YES':
         for each in os.listdir(os.getcwd()):
             if os.path.splitext(each)[1] == '.txt':
                 f = open(os.getcwd() + '/' + each)
                 strs = f.read()
                 if key in strs:
                     print('在文件',os.getcwd() + '/' + each + '中找到关键字：' + key)
                     f.seek(0)
                     l1 = f.readlines()
                     length = len(l1)
                     for line in range(length):
                         s1 = l1[line]
                         if key in s1:
                             pos = []
                             begin = s1.find((key))
                             while begin != -1:
                                pos.append(begin+1)
                                begin = s1.find(key,begin+1)
                             print('关键字出现在第',line+1,'行，第',pos,'个位置。')
                 f.close()
             if os.path.isdir(each):
                 os.chdir(each)
                 search(key,yup)
                 os.chdir(os.pardir)
key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
# yup = input('请问是否需要打印关键字[ %s ]在文件中的具体位置(YES/NO)： ' % key)
yup = input('请问是否需要打印关键字[ {0} ]在文件中的具体位置(YES/NO)： '.format(key))
search(key,yup)

