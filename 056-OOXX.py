import urllib.request
import os
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

def get_url(html):
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    pgnum = int(html[a:b])
    return pgnum

def get_img_url(pgurl):
    img_list = []
    html = open_url(pgurl).decode('utf-8')
    a = html.find('mg src=')
    while a != -1:
        b = html.find('.jpg',a ,a +255)
        if b != -1:
            img_list.append('http://' + html[a+10:b+4])
        else:
            b = a + 11
        a = html.find('mg src=', b)
    return img_list

def save_img(folder, img_list):
    for each in img_list:
        filename = each.split('/')[-1]
        try:
            html = open_url(each)
        except:
            continue
        with open(filename, 'wb') as f:
            f.write(html)

def download_mm(folder='OOXX',pages=10):
    url = 'http://jandan.net/ooxx/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)
    html = open_url(url).decode('utf-8')
    pgnum = get_url(html)
    for i in range(pages):
        pgnum -= i
        pgurl = url + 'page-' + str(pgnum) + '#comments'
        get_img_url(pgurl)
        img_list = get_img_url(pgurl)
        save_img(folder, img_list)

if __name__ == '__main__':
    download_mm(folder='OOXX', pages=10)



