###请复制到交互模式下执行代码：
import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print('现在的坐标是：',self.x,self.y)

class GoldFish(Fish):
    pass

class selmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)   ### 调用未绑定的方法继承父类的属性或方法，缺点在于如果父类改变，每次都要修改.__init__(self)之前的父类名；
        super().__init__()  ###调用super函数直接继承父类的方法，与未绑定方法的差异在于：不用指定父类，它自己会去继承所有父类的方法，如果父类改变，只要改变 class 语句里的父类即可；
        self.hungry = True
    def eat(self):
        if self.hungry == True:
            print('我要吃东西，饿的慌!')
            self.hungry = False
        else:
            print('涨成了猪！')



