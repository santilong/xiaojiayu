import easygui as g
import sys
import os
path = g.fileopenbox('选择要打开的文件','选择文件',default='*.txt')
print(path)
flag = 0
with open(path,encoding='utf8') as f:
    title = os.path.split(path)[1]
    # title = os.path.basename(path)
    msg = '文件{0}的内容如下：'.format(title)
    text = f.read()
    print(text)
    ntext = g.textbox(msg,'显示文件内容',text=text)
    print(ntext)
    oldl = len(text)
    newl = len(ntext)
    if oldl > newl:
        flag = 1
    elif oldl< newl:
        flag = 1
    else:
        for each in range(oldl):
            if text[each] != ntext[each]:
                flag = 1
    if flag == 1:
        tag = g.indexbox('捡到到文件内容发生改变，请选择以下操作','警告',choices=('覆盖保存','放弃保存','另存为...'))
    else:
        sys.exit(0)
if tag == 0:
    with open(path,'w',encoding='utf8') as f:
        f.write(ntext)
elif tag == 1:
    sys.exit(0)
else:
    filename = g.enterbox('请输入要保存的文件名：','另存为',default='new' + title)
    newfilename = os.path.dirname(path) + '/' + filename
    # f2 = open(newfilename,'w')
    with open(newfilename,'w') as f2:
        f2.write(ntext)
    # f2.close()







