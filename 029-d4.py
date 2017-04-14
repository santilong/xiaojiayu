name = input('请输入文件名： ')
f = open(name,'w+')
str1 = input('请输入需要替换的单词或字符： ')
str2 = input('请输入新的单词或字符： ')
str3 = f.read()
# print(str3)
print('文件',name,'中共有',str3.count(str1),'个',str1)
print('您确定要把所有的[',str1,']替换为[',str2,']吗？ ')
if input('YES/NO： ') == 'yes' or input('YES/NO： ') == 'YES':
    str3.replace(str1,str2)
    f.writelines(str3)
else:
    pass
f.close()