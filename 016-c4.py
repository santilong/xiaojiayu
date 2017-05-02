name = input('请输入查找的用户名：')
score = [['A',85],['B',80],['C',65],['D',95],['E',90]]
flog = 0
for each in score:
      if name == each[0]:
            #print(name + '的得分是：',each[1])
            print(name,'的得分是：',each[1])
            flog = 1
            break
if flog == 0:
      print('查找的数据不存在')
            
