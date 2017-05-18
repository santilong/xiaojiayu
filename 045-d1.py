#coding: utf-8
'''编写 Demo 类，使得下边代码可以正常执行：
>>> demo = Demo()
>>> demo.x
'FishC'
>>> demo.x = "X-man"
>>> demo.x
'X-man'
'''

'''分析：
1、Demo()类本身没有x属性，所以需要编写__getattr__魔法方法；
2、demo.x = 'X-man'属性赋值，可以直接使用基类的__setattr—__魔法方法实现；
'''

class Demo():
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name

d = Demo()
d.x ===> FishC ###当获取不存在的属性x时直接返回'FishC'
d.x = 'X-man'   ###这里没有重载__setattr__，赋值操作直接调用基类的__setattr__
d.x ===> X-man  ###因为x通过基类的__setattr__赋值，再通过基类的__getattribute__获取；


