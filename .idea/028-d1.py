'''将小甲鱼给的OpenMe.mp3保存为新文件OpenMe.txt'''
f1 = open('/Users/longyue/Downloads/OpenMe.mp3','br')
f2 = open('/Users/longyue/Downloads/OpenMe.txt','w+')
# f2.writelines(f1.read())
f2.write(f1.read())
f1.close()
f2.close()
