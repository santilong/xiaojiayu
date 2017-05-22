'''
用while语句实现与以下for语句相同的功能：
for each in range(5):
    print(each)
'''

#coding: utf-8

i1 = iter(range(5))
while True:
    try:
        each = next(i1)
    except StopIteration:
        break
    print(each)

