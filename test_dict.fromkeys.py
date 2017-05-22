'''字典的fromkeys方法验证'''
l1 = ['x','y','z']
d1 = dict.fromkeys(l1,0)
print(d1)
d1['x'] += 2
print(d1)