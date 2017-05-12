#coding: utf-8
'''定义一个类，当实例化该类的时候，自动判断传入了多少个参数，并显示出来。'''
class C:
    count = 0
    def __init__(self, *args, **kwargs):
        if not args or not kwargs:
            print('没传入任何参数！')
        else:
            C.count += len(args)
            C.count += len(kwargs)
            print('传入了' + str(C.count) + '个参数，分别是' + str(args) + str(kwargs))

# c = C()
c = C(1,2,3,x = 9, y = 0)
