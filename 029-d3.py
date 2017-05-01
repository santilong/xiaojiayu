f = open(input('请输入要打开的文件(c:\\test.txt)：'))
strs = input('请输入需要显示的行数 [ 格式如 13:21 或 :21 或 21: ] ： ')
start,end = strs.split(':')
list1 = f.readlines()
for i in range(int(start)-1,int(end)):
    print(list1[i])
f.close()