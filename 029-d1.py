f1 = open(input('请输入需要比较的头一个文件名：'))
f2 = open(input('请输入需要比较的另一个文件名：'))
l1 = f1.readlines()
l2 = f2.readlines()
len1 = len(l1)
len2 = len(l2)
n = 0
l3 = []
if len1 == len2:
    for i in range(len1):
        if l1[i] == l2[i]:
            pass
        else:
            n += 1
            l3.append(i)
else:
    max = len1 if len1 > len2 else len2
    for i in range(max):
        if l1[i:i+1] == l2[i:i+1]:
            pass
        else:
            n += 1
            l3.append(i+1)
print('两个文件共有' + '[' + str(n) + ']处不同：')
for i in l3:
    print('第',i,'行不一样')
f1.close()
f2.close()

