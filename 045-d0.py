#coding: utf-8
'''方法一：'''
class C:
    def __getattribute__(self,name):
        print('调用__getattribute__')
        return super().__getattribute__(name)   ###因为是获取属性的值，所以这里需要用return返回；
    def __getattr__(self,name):
       print('该属性不存在')
    def __setattr__(self, name, value):
        print('设置属性！')
        super().__setattr__(name,value)     ###这里不需要return，因为不用到值；
    def __delattr__(self, name):
        print('删除属性')
        super().__delattr__(name)
c = C()
c.x
c.x = 10

'''方法二：

class C:
    def __getattribute__(self,name):
        print('调用__getattribute__')
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        print('设置属性！')
        super().__setattr__(name,value)
    def __delattr__(self, name):
        print('删除属性')
        super().__delattr__(name)

try:
    c = C()
    c.x
except AttributeError as e:
    pirnt('该属性不存在')

'''

