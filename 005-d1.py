#!/usr/bin/env python
#coding:utf-8

year = input("请输入年份，格式为YYYY：")
if (year % 4 == 0 and year % 100 != 0):
	print("%d 为闰年" % year)
else:
	print("%d不为闰年" % year)





