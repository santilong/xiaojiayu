import easygui as eg
import urllib.request
l1 = eg.multenterbox(msg='请填写喵的尺寸', title='下载一只喵',fields=['宽', '高'], values=[400,600])
url = 'http://placekitten.com/g/' + l1[0] + '/' + l1[1]
# print(url)
res = urllib.request.urlopen(url)
cat_img = res.read()
dir = eg.diropenbox(msg='请选择存放喵的文件夹',title='浏览文件夹')
with open(dir + '/cat_img' + l1[0] + '-' + l1[1], 'wb') as f:
    f.write(cat_img)




