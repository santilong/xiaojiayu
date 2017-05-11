#coding: utf-8
class Temp(float):
    def __new__(cls,temp): ###这里的cls就是Temp这个类，将Temp类做为父类float的第一个参数传入父类的__new__中，创建一个实例化对象；
        return float.__new__(cls,temp * 1.8 + 32)   ###然后返回这个实例化对象的__new__方法的结果
print(Temp(32))

'''也可改写为如下'''
class Temp(float):
    def __new__(cls,temp):
        return super(Temp,cls).__new__(cls, temp * 1.8 +32) '''super(Temp,cls)表示通过Temp这个子类找到父类，
                                                               然后将Temp类的对象cls转化为父类float的对象，最
                                                               后返回这个对象的__new__()的结果'''
print(Temp(32))
