def count(*args):
    for param in args:
        yw = 0
        kg = 0
        num = 0
        oth = 0
        for each in param:
            if each.isdigit():
                num += 1
            elif each.isalpha():
                yw += 1
            elif each.isspace():
                kg += 1
            # elif not (each.isdigit() and each.isalpha() and each.isspace()):
            else:
                oth += 1
        print('\'',param,'\'','的数字的个数为：%d,英文的个数为：%d,空格的个数为：%d,其他字符的个数为：%d' % (num, yw, kg, oth))

count('I love fishc.com.','I love you, you love me.')

###以下为小甲鱼的答案：
# def count(*param):
#     length = len(param)
#     for i in range(length):
#         letters = 0
#         space = 0
#         digit = 0
#         others = 0
#         for each in param[i]:
#             if each.isalpha():
#                 letters += 1
#             elif each.isdigit():
#                 digit += 1
#             elif each == ' ':
#                 space += 1
#             else:
#                 others += 1
#         print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i + 1, letters, digit, space, others))
#
#
# count('I love fishc.com.', 'I love you, you love me.')
