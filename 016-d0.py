def minx(l1):
      temp = l1[0]
      for i in l1[1:]:
            if i < temp:
                  temp = i
      return temp
l1 = '123456789'
a = minx(l1)
print(a)
                  
