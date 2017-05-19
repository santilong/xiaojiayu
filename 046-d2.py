# #coding: utf-8
# import pickle
# import os
#
# class MyDes:
#     def __init__(self, arg, value=0):
#         self.arg = arg
#         self.value = value
#     def __get__(self, instance, owner):
#         return self.value
#     def __set__(self, instance, value):
#         self.value = value
#         f = open(self.arg + '.pkl', 'wb')
#         pickle.dump(self.value, f)
#         f.close()
#         print('已写入，关闭文件！！！')
#     def __delete__(self, instance):
#         os.remove(self.arg + '.pkl')
#         del self.arg
#
# class Test:
#     x = MyDes('x')
#     y = MyDes('y')

import os
import pickle

class MyDes:
    saved = []

    def __init__(self, name = None):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.filename, 'rb') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)



