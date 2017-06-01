'''编写一个爬虫，爬百度百科“网络爬虫”的词条（链接 -> http://baike.baidu.com/view/284853.htm），将所有包含“view”的链接按下边格式打印出来。'''
import urllib.request
from bs4 import BeautifulSoup
import re
url = 'http://baike.baidu.com/view/284853.htm'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
# print(html)
soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all(href=re.compile(r'view')):
    print(link.text, '--->', ''.join(['http://baike.baidu.com', link['href']]))

