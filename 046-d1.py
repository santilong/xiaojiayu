'''按要求编写描述符 MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件：record.txt'''
#coding: utf-8
import time
def writeopt(var):
    with open('record_for_046.txt','a+') as f:
        f.writelines(var)

class MyDes:
    def __init__(self, value, arg):
        self.value = value
        self.arg = arg
    def __get__(self, instance, owner):
        self.ctime = time.ctime()
        var = self.arg + '变量于北京时间' + self.ctime + '被读取，' + self.arg + '=' + str(self.value) + '\n'
        writeopt(var)
        return self.value

    def __set__(self, instance, value):
        self.value = value
        self.ctime = time.ctime()
        var = self.arg + '变量于北京时间' + self.ctime + '被修改，' + self.arg + '=' + str(self.value) + '\n'
        writeopt(var)
        return self.value

class Test:
    x = MyDes(10, 'x')
    y = MyDes(8.8, 'y')

test = Test()
test.x
test.y
test.x = 123
test.x = 1.23
test.y = 'I love santi !'
