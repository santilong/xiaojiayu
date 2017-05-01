list1 = ['1.Jost do It', '2.一切皆有可能', '3.让编程改变世界', '4.Impossible is Nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼C工作室','1.耐克']

list3 = [(y + ':'+ x.split('.')[1]) for x in list1 for y in list2 if x.split('.')[0] == y.split('.')[0]]
for each in list3:
      print(each)
print('\n')
list4 = [name +':' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
for each in list4:
      print(each)
