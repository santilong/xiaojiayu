var = ' Hi '

def fun1():
    global var
    var = ' Baby '
    print('func1', var)
    def fun2():
        var = 'I love you'
        print('func2', var)
        # def fun3():
        #     nonlocal var
        #     var = ' 小甲鱼 '
        #     # print('func3', var)
        #
        # fun3()
    return var
    # return fun2()
print(fun1())
