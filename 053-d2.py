#coding: utf-8
import urllib.request
import chardet
import os

num = 1
with open(os.getcwd() + '/urls.txt') as f1:
    urls = f1.read().splitlines()
    for url in urls:
        print(url)
        res = urllib.request.urlopen(url).read()
        res = res.decode(chardet.detect(res)['encoding'])
        with open(os.getcwd() + '/url_' + str(num) + '.txt', 'w') as f2:
            f2.write(res)
        num += 1
