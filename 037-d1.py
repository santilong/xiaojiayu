import random as r
direX = [0,10]
direY = [0,10]
class Turtle:
    def __init__(self):
        self.power = 100    ###初始体力
        self.x = r.randint(direX[0],direX[1])   ###初始X坐标
        self.y = r.randint(direY[0],direY[1])   ###初始Y坐标
    def move(self):
        new_x = self.x + r.choice([-2, -1, 1, 2])
        new_y = self.y + r.choice([-2, -1, 1, 2])
        ###检查X坐标是否超出范围
        if new_x < direX[0]:
            self.x = direX[0] - (new_x - direY[0])
        elif new_x > direX[1]:
            self.x = direX[1] - (new_x - direX[1])
        else:
            self.x = new_x
        ###检查Y坐标是否超出范围
        if new_y < direY[0]:
            self.y = direY[0] - (new_y - direY[0])
        elif new_y > direY[1]:
            self.y = direY[1] - (new_y - direY[1])
        else:
            self.y = new_y
        ###体力消耗；
        self.power -= 1
        return (self.x, self.y)
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(direX[0],direX[1])
        self.y = r.randint(direY[0],direY[1])
    def move(self):
        new_x = self.x + r.choice([-1, 1])
        new_y = self.y + r.choice([-1, 1])

        if new_x < direX[0]:
            self.x = direX[0] - (new_x - direX[0])
        elif new_x > direX[1]:
            self.x = direX[1] - (new_x - direX[1])
        else:
            self.x = new_x

        if new_y < direY[0]:
            self.y = direY[0] - (new_x - direY[0])
        elif new_y > direY[1]:
            self.y = direY[1] - (new_x - direY[1])
        else:
            self.y = new_y
        return (self.x, self.y)

tt = Turtle()
fish = []
for i in range(10):
    new_fs = Fish()
    fish.append(new_fs)


while True:
    if not len(fish):
        print('鱼儿被吃完了！')
        break
    if not tt.power:
        print('乌龟体力耗尽，挂掉了！')
        break
    pos = tt.move()
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            tt.eat()
            fish.remove(each_fish)
            print('有一根鱼儿被乌龟吃掉了！')
























