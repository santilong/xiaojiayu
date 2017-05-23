#coding: utf-8

def Rev(var):
    index = len(var) - 1
    while index:
        yield var[index]
        index -= 1
    yield var[index]

rev = Rev('FishC')
for each in rev:
    print(each,end='')


