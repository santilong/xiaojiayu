def findstr(strs,sub):
    return strs.count(sub)
strs = input('请输入字符串1：')
sub = input('请输入字符串2：')
print(sub + '在' + '\'' +  strs + '\'' + '中出现的次数为：',findstr(strs,sub))