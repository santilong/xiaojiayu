import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
data = {}
word = input('请输入要查询的关键词：')
data['word'] = word

data = urllib.parse.urlencode(data)
url = 'http://baike.baidu.com/search/word?%s' % data
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
# print(html)
soup = BeautifulSoup(html, 'lxml')
for link in soup.find_all(href=re.compile(r'view')):
    content = link.text
    url2 = ''.join(['http://baike.baidu.com',link['href']])
    res2 = urllib.request.urlopen(url2)
    html2 = res2.read().decode('utf-8')
    soup2 = BeautifulSoup(html2, 'lxml')
    if soup2.h2:
        content += soup2.h2.text
    content = content + '->' + url2
    print(content)
    # print(link.text, '--->', ''.join(['http://baike.baidu.com',link['href']]))

# import urllib.request
# import urllib.parse
# import re
# from bs4 import BeautifulSoup
#
# def main():
#     keyword = input("请输入关键词：")
#     keyword = urllib.parse.urlencode({"word":keyword})
#     response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
#     html = response.read()
#     soup = BeautifulSoup(html, "html.parser")
#
#     for each in soup.find_all(href=re.compile("view")):
#         content = ''.join([each.text])
#         url2 = ''.join(["http://baike.baidu.com", each["href"]])
#         response2 = urllib.request.urlopen(url2)
#         html2 = response2.read()
#         soup2 = BeautifulSoup(html2, "html.parser")
#         if soup2.h2:
#             content = ''.join([content, soup2.h2.text])
#         content = ''.join([content, " -> ", url2])
#         print(content)
#
# if __name__ == "__main__":
#     main()