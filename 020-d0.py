f = open('/Users/longyue/Downloads/string1.txt','r')
strs = f.read()
list1 = []
for each in strs:
    if each not in list1:
        if each == '\n':
            print('\\n',strs.count(each))
        else:
            print(each,strs.count(each))
        list1.append(each)

f.close()



# ###以下为小甲鱼的答案：
# f = open('/Users/longyue/Downloads/string1.txt','r')
# str1 = f.read()
# list1 = []
# for each in str1:
#     if each not in list1:
#         if each == '\n':
#             print('\\n', str1.count(each))
#         else:
#             print(each, str1.count(each))
#         list1.append(each)
# f.close()