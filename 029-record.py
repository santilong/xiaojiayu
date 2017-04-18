#coding:utf-8
boys = []
girls = []
n = 1
f = open('record.txt','r+',encoding='cp936')
for each in f.readlines():
    if each[0:6] != '======':
        rule,content = each.split(':',maxsplit=1)
        if rule == '小客服':
            girls.append(content)
        elif rule == '小甲鱼':
            boys.append(content)
    else:
        girl = open('girl_' + str(n) + '.txt', 'w')
        boy = open('boy_' + str(n) + '.txt', 'w')
        girl.writelines(girls)
        boy.writelines(boys)
        boy.close()
        girl.close()
        boys = []
        girls = []
        n += 1
girl = open('girl_' + str(n) + '.txt', 'w')
boy = open('boy_' + str(n) + '.txt', 'w')
girl.writelines(girls)
boy.writelines(boys)
boy.close()
girl.close()
f.close()