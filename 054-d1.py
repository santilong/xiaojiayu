'''python登录豆瓣'''
import urllib.request, re
import urllib.parse
import http.cookiejar
import easygui as eg
url = 'https://accounts.douban.com/login'
cookie = http.cookiejar.CookieJar() ###创建cookie对象;
handler = urllib.request.HTTPCookieProcessor(cookie)    ###创建cookie的触发器；
opener = urllib.request.build_opener(handler)   ###创建opener
###创建提交表单字典###
data = {}
data['source'] = 'index_nav'
data['form_email'] = 'ly631@163.com'
data['form_password'] = '520Wy1314'
###################
opener.addheaders = [('User-Agent','ooxx')]
res = opener.open(url, urllib.parse.urlencode(data).encode('utf-8'))
html = res.read().decode('utf-8')
m = re.search('<img id="captcha_image" src="(.*)" alt="captcha" class="captcha_image"/>', html)
if m:
    imgurl = m.group(1)
    urllib.request.urlretrieve(imgurl, 'captcha_image.gif')
    n = re.search('<input type="hidden" name="captcha-id" value="(.*)"/>', html)
    if n:
        content = eg.enterbox(msg='请输入图上的验证码', title='验证码输入')
        ###扩充提交表单字典，以支持验证码；
        data['captcha-solution'] = content
        data['captcha-id'] = n.group(1)
        #############################
        res1 = opener.open(url, urllib.parse.urlencode(data).encode('utf-8'))
        if res1.geturl() == 'https://www.douban.com/':
            print('登录成功')






