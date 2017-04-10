def huiwenlian(strs):
    temp = len(strs)
    last = temp - 1
    temp //= 2
    flag = 1
    for each in range(temp):
        if strs[each] != strs[last]:
            flag = 0
        last -= 1
    if flag == 1:
        return 1
    else:
        return 0
strs = input('请输入一句话：')
if huiwenlian(strs) == 1:
    print('是回文联')
else:
    print('不是回文联')

