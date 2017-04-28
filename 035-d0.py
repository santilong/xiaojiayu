import random
import easygui as g

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
temp = g.enterbox('不妨猜一下小甲鱼现在心里想的是哪个数字(1-10)）：','请输入数字',strip=True)
guess = int(temp)
while guess != secret:
    # temp = input("哎呀，猜错了，请重新输入吧：")
    temp = g.enterbox('哎呀，猜错了，请重新输入吧：', '请输入数字', strip=True)
    guess = int(temp)
    if guess == secret:
        # print("我草，你是小甲鱼心里的蛔虫吗？！")
        # print("哼，猜中了也没有奖励！")
        g.msgbox('我草，你是小甲鱼心里的蛔虫吗？！')
        g.msgbox('哼，猜中了也没有奖励！')
    else:
        if guess > secret:
            g.msgbox('哥，大了大了~~~')
            # print("哥，大了大了~~~")
        else:
            # print("嘿，小了，小了~~~")
            g.msgbox('嘿，小了，小了~~~')
# print("游戏结束，不玩啦^_^")
g.msgbox('游戏结束，不玩啦^_^')
