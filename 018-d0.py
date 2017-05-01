def test(*args,base=3):
      sum = 0
      for each in args:
            sum += each
      sum *= base
      print(sum)
test(1,2,3,4,5,base=5)          
            

