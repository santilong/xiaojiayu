import os
txt = 0
png = 0
py = 0
docx = 0
dir = 0
for each in os.listdir():
    if os.path.isdir(each):
        dir += 1
    elif os.path.isfile(each):
        type = os.path.splitext(each)[1]
        if type == '.txt':
            txt += 1
        elif type == '.png':
            png += 1
        elif type == '.py':
            py += 1
        elif type == '.docx':
            docx += 1
print('该文件夹下共有类型为[.txt]的文件',txt,'个。')
print('该文件夹下共有类型为[.png]的文件',png,'个。')
print('该文件夹下共有类型为[.py]的文件',py,'个。')
print('该文件夹下共有类型为[.docx]的文件',docx,'个。')
print('该文件夹下共有类型为[文件夹]的文件',dir,'个。')