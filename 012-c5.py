list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
list2 = []
for x in range(10):
      for y in range(10):
            if x % 2 == 0:
                  if y % 2 != 0:
                        list2.append((x,y))
print('list1 is:',list1)
print('list2 is:',list2)
if list1 == list2 :
      print('完全正确！')



