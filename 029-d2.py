f = open(input('请输入要打开的文件(c:\\test.txt)：'))
num = int(input('请输入要显示该文件的前几行：'))

# l1 = f.readlines()
# for i in range(num):
#     print(l1[i],end='\n')

for i in range(num):
    print(f.readline())


f.close()