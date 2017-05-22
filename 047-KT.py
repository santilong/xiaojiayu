'''编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数'''
#coding: utf-8

class CountList:
    def __init__(self, *args):
        self.value = [x for x in args]
        self.count= {}.fromkeys(range(len(self.value)), 0)
    def __len__(self):
        return len(self.value)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.value[key]

