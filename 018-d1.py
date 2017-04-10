def shuixianhuashu():
    for each in range(1,1000):
        temp = each
        sum = 0
        while temp:
            sum += (temp % 10) ** 3
            temp = temp // 10
            if sum == each:
                print(each, '是水仙花数')
shuixianhuashu()