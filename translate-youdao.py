#coding: utf-8
import urllib.request
import urllib.parse
import json
import sys
# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=dict2.index'
content = '日了狗'
# content = sys.argv[1]
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1495814193843'
data['sign'] = '1d8524d351590488b4b0c1809e09e38a'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
res = urllib.request.urlopen(url, data)
html = res.read().decode('utf-8')
html = json.loads(html)
print(html['translateResult'][0][0]['tgt'])




# import urllib.request
# import urllib.parse
# import json
#
# class Translate():
#     def __init__(self):
#         self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
#             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
#         # Form Data
#         self.data = {}
#         self.data['type'] = 'AUTO'
#         self.data['i'] = 'python 语言'# 翻译文本
#         self.data['doctype'] = 'json'
#         self.data['xmlVersion'] = '1.8'
#         self.data['keyfrom'] = 'fanyi.web'
#         self.data['ue'] = 'UTF-8'
#         self.data['action'] = 'FY_BY_CLICKBUTTON'
#         self.data['typoResult'] = 'true'
#
#     def tanslate(self,words):
#         self.data['i'] = words
#         data = urllib.parse.urlencode(self.data).encode('utf-8')
#         response = urllib.request.urlopen(self.url,data)
#
#         # 解析json字符串
#         html = response.read().decode('utf-8')
#         target = json.loads(html)
#         return target['translateResult'][0][0]['tgt']
#
# if __name__=='__main__':
#     trans = Translate()
#     result = trans.tanslate('开源中国')
#     print(result)