for i in range(100,999):
      n1 = int(str(i)[0])
      n2 = int(str(i)[1])
      n3 = int(str(i)[2])
      if (n1 **3) + (n2 ** 3) + (n3 ** 3) == i:
            print('%d为水仙花数!' % i)
