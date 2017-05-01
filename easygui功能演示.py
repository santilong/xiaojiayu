import easygui as g
import sys
import os

###easygui展示函数
# g.egdemo()
###

###easygui默认参数，对于所有函数而言，前两个参数是消息和标题。
# g.ccbox()
###

###choicebox函数及easygui可以使用关键字参数
# choices = ('愿意','不愿意','有钱的时候愿意')
# choice = g.choicebox(title='ooxx',msg='你愿意购买资源包么？',choices=choices)
###

###msgbox函数，语法：msgbox(msg='(Your message goes here)', title=' ', ok_button='OK', image=None, root=None);ok_button为OK按钮的显示内容，可自定义；
# g.msgbox('你好','清晨',ok_button='WTF')
###

###ccbox函数，语法：ccbox(msg='Shall I continue?', title=' ', choices=('Continue', 'Cancel'), image=None);
###ccbox() 提供一个选择：Continue 或者 Cancel，并相应的返回 1（选中Continue）或者 0（选中Cancel）。
# if g.ccbox('要再完一次吗？','选择',choices=('再玩一次','不玩了')):
#     g.msgbox('不给玩了，再玩都玩坏了！')
# else:
#     sys.exit(0)
###

###ynbox函数，与ccbox一模一样，语法：ynbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None)
# g.ynbox('要出门了吗？','选择',choices=('出门','不出门'))
###

###buttonbox函数，语法：buttonbox(msg='', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None)
# g.buttonbox('你喜欢哪种水果？','水果选择',choices=('苹果','芒果','火龙果'))
###

###indexbox函数，与buttonbox一样，区别是当用户选择第一个按钮的时候返回序号 0， 选择第二个按钮的时候返回序号 1;
### 语法：ndexbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None),
# indexnum = g.indexbox('你喜欢哪种水果？','水果选择',choices=('苹果','芒果','火龙果'))
# print(indexnum)
###

###boolbox函数，语法：boolbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None);
###如果第一个按钮被选中则返回 1，否则返回 0。
# flag = g.boolbox('test','测试页',choices=('是','否'))
# print(flag)
###

###buttonbox、msgbox、indexbox、ynbox中添加图片，关键字参数image='.gif'，注意，仅支持GIF格式；
g.msgbox(msg='可耻的硬了',title='生理反应',image='111.gif')
###

###choicebox函数，语法：choicebox(msg='Pick something.', title=' ', choices=())；
###参数choices为序列(元组或列表)
# choice = ['.DS_Store','030-d1.py','030-d2.py','030-d3.py','030-d4.py']
# cho = g.choicebox(msg='OOXX否？',title='选择',choices=choice)
# print(cho)
###

###multchoicebox函数，语法：multchoicebox(msg='Pick as many items as you like.', title=' ', choices=(), **kwargs);
###multchoicebox() 函数也是提供一个可选择的列表，与 choicebox() 不同的是，multchoicebox() 支持用户选择 0 个，1 个或者同时选择多个选项。
# choice = ['.DS_Store','030-d1.py','030-d2.py','030-d3.py','030-d4.py']
# cho = g.multchoicebox('OOXX否？','选择',choices=choice)
# print(cho)
###

###enterbox函数，语法：enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None);
###enterbox() 为用户提供一个最简单的输入框，返回值为用户输入的字符串。默认返回的值会自动去除首尾的空格，如果需要保留首尾空格的话请设置参数 strip=False。
# inp = g.enterbox('请任意输入','输入',image='111.gif',strip=False,default='请任意输入')
# print(inp)
###

###integerbox函数，语法：integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments);
###integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbound参数设置最小值，upperbound参数设置最大值）的整型数值，否则会要求用户重新输入。
# inte = g.integerbox('请输入：','输入窗口',default='0',lowerbound=0,upperbound=150,image='111.gif')
# print(inte)
###

###multenterbox函数，语法：multenterbox(msg='Fill in values for the fields.', title=' ', fields=(), values=());
###
# mulenter = g.multenterbox('test','多框输入窗口',fields=[1,2,3,4,5],values=[111,222,333,444,555],)
# print(mulenter)
###

###passwordbox函数，语法：passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None);
###与enterbox函数类似，只是输入的内容显示为***;
# pw = g.passwordbox(msg='请输入密码！',title='密码',image='111.gif')
# print(pw)
###

###multpasswordbox函数，语法：multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=());
###与multenterbox类似，只是最后一个输入框显示为密码形式"***"；
# info = g.multpasswordbox('请输入账户和密码','登录',fields=['账户：','密码：'])
# print(info)
###

###textbox函数，语法：textbox(msg='', title=' ', text='', codebox=0);
###textbox() 函数默认会以比例字体（参数 codebox=1 设置为等宽字体）来显示文本内容（会自动换行哦），这个函数适合用于显示一般的书面文字。
###text 参数（第三个参数）可以是字符串类型，列表类型，或者元祖类型。
# content = ['dir(int)','__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
# g.textbox('显示以下内容：','文本显示',text=content,codebox=0)
###

###codebox函数，语法：codebox(msg='', title=' ', text='')
# code = '''while 1:
#     g.msgbox('嗨，欢迎进入第一个界面小游戏！')
#     msg = '请问你希望学习到什么知识？'
#     title = '小游戏互动'
#     choices = ['OOXX','啪啪啪','打饼子','行房事']'''
# g.codebox('代码如下：','代码查看',text=code)
###

###diropenbox函数，语法：diropenbox(msg=None, title=None, default=None)
###返回用户选择的目录名（带完整路径哦）
# path = g.diropenbox('选择路径','路径')
# print(path)
###

###fileopenbox函数，语法：fileopenbox(msg=None, title=None, default='*', filetypes=None);
###返回用户选择的文件名（带完整路径哦）
###filetypes
# file = g.fileopenbox(default="*.py")
# print(file)
###

###filesavebox函数，语法：filesavebox(msg=None, title=None, default='', filetypes=None)
###让用于选择文件需要保存的路径（带完整路径哦）
# filedir = g.filesavebox(default="*")
# print(filedir)
###

# ###存储用户设置；
# ###settings类：
# ###定义Settings类：
# class Settings(g.EgStore)
#
#
#
# settingsfile = os.path.join(os.getcwd(),'settings')
# settings = Settings(settingsfile)
# ###定义需要存储的用户变量：
# user = 'santi'
# server = 'Home'
# settings.userId = user
# settings.targetServer = server
# ###持久存储用户变量：
# settings.store()

###异常捕获exceptionbox函数；
# try:
#     int('santi')
# except:
#     g.exceptionbox()
###






























