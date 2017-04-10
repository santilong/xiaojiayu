f = open('/Users/longyue/Downloads/string2.txt','r')
strs = f.read()
list1 = []
n = 0
for each in strs:
    flag = 1
    if each == '\n':
        continue
    if each.islower():
        index = strs.index(each,n)
        if index >= 4 and (index+4) <= len(strs):
            ooo = strs[index-4:index-3]
            kkk = strs[index+4:index+5]
            if strs[index-4:index-3].islower() and strs[index+4:index+5].islower():
                for a in strs[index-3:index]:
                    if not a.isupper():
                        flag = 0
                for b in strs[index+1:index+4]:
                    if not b.isupper():
                        flag = 0
                if flag == 1:
                    list1.append(each)
    n += 1
f.close()
print(''.join(list1))





###以下为小甲鱼的答案：
# f = open('/Users/longyue/Downloads/string2.txt','r')
# str1 = f.read()
# str1 = '''BgEmDSKiJKLkkzFWlobXIettjTJNlHZYlJZRRoKXExTRtzSKLoIOScEwBCDvWF'''
#
#
# countA = 0  # 统计前边的大写字母
# countB = 0  # 统计小写字母
# countC = 0  # 统计后边的大写字母
# length = len(str1)
#
# for i in range(length):
#     if str1[i] == '\n':
#         continue
#
#     """
#     |如果str1[i]是大写字母：
#     |-- 如果已经出现小写字母：
#     |-- -- 统计后边的大写字母
#     |-- 如果未出现小写字母：
#     |-- -- 清空后边大写字母的统计
#     |-- -- 统计前边的大写字母
#     """
#     if str1[i].isupper():
#         if countB:
#             countC += 1
#         else:
#             countC = 0
#             countA += 1
#
#     """
#     |如果str1[i]是小写字母：
#     |-- 如果小写字母前边不是三个大写字母（不符合条件）：
#     |-- -- 清空所有记录，重新统计
#     |-- 如果小写字母前边是三个大写字母（符合条件）：
#     |-- -- 如果已经存在小写字母：
#     |-- -- -- 清空所有记录，重新统计（出现两个小写字母）
#     |-- -- 如果该小写字母是唯一的：
#     |-- -- -- countB记录出现小写字母，准备开始统计countC
#     """
#     if str1[i].islower():
#         if countA != 3:
#             countA = 0
#             countB = 0
#             countC = 0
#         else:
#             if countB:
#                 countA = 0
#                 countB = 0
#                 countC = 0
#             else:
#                 countB = 1
#                 countC = 0
#                 target = i
#
#     """
#     |如果前边和后边都是三个大写字母：
#     |-- 如果后边第四个字母也是大写字母（不符合条件）：
#     |-- -- 清空记录B和C，重新统计
#     |-- 如果后边仅有三个大写字母（符合所有条件）：
#     |-- -- 打印结果，并清空所有记录，进入下一轮统计
#     """
#     if countA == 3 and countC == 3:
#         if i+1 != length and str1[i+1].isupper():
#             countB = 0
#             countC = 0
#         else:
#             print(str1[target], end='')
#             countA = 3
#             countB = 0
#             countC = 0
#
#
#
#
#
