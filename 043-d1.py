#coding: utf-8
'''定义一个单词（Word）类继承自字符串，重写比较操作符（参考自学：Python 魔法方法详解），当两个 Word 类对象进行比较时，根据单词的长度来进行比较大小。J1'''
class Word(str):
    def __new__(cls,var):
        if ' ' in var:
            var = var[:var.index(' ')]
        return str.__new__(cls,var)
    def __lt__(self,other):
        return len(self) < len(other)
    def __gt__(self,other):
        return len(self) > len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

a = Word('hello world')
b = Word('oo xx')
print(a > b)
print(a < b)