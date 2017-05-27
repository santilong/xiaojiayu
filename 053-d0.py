import urllib.request
res = urllib.request.urlopen('http://www.fishc.com')
html = res.read(300)
html = html.decode('utf-8')
print(html)