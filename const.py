#coding: utf-8
# class Const:
#     COUNT = 0
#     def __setattr__(self, key, value):
#         if key == 'NAME' and Const.COUNT != 0:
#             raise TypeError('变量名无法改变！')
#         elif str(key).islower():
#             raise TypeError('变量名需要大写')
#         else:
#             super().__setattr__(key, value)
#             Const.COUNT += 1
#
# const = Const()

# 该模块用于让 Python 支持常量操作
class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError('常量无法改变！')

        if not name.isupper():
            raise TypeError('常量名必须由大写字母组成！')

        self.__dict__[name] = value


import sys

sys.modules[__name__] = Const()

