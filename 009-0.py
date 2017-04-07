#!/usr/bin/env python
#coding: utf-8
passwd = str(input('请输入密码：'))
n = 1
passd = '666'
while n <= 3:
	if '*' in passwd:
		print('密码中不能包含*，你还有3次机会!')
	passwd = str(input('请输入密码：'))
	if passwd == passd:
		print('密码正确，进入程序...')
	n += 1
