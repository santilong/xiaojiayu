import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎进入第一个界面小游戏！')

    msg = '请问你希望学习到什么知识？'
    title = '小游戏互动'
    choices = ['OOXX','啪啪啪','打饼子','行房事']

    choice = g.choicebox(msg,title,choices)
    g.msgbox('你的选择是' + choice,'结果')
    msg = '你希望重新开始小游戏么？'
    title = '请选择'

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)

