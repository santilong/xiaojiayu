def register(name):
    while True:
        if not name in user.keys():
            password = input('请输入密码：')
            user[name] = password
            print('注册成功，赶紧试试登录吧.')
            break
        else:
            name = input('此用户名已被使用，请重新输入：')
            continue

def login(name):
    while True:
        if name not in user.keys():
            name = input('您输入的用户名不存在，请重新输入：')
            continue
        else:
            password = input('请输入密码：')
            if password == user.get(name):
                print('欢迎进入OOXX系统，请点右上角的x结束程序!')
            else:
                print('密码错误!')
            break

def main():
    while 1:
        print('|--- 新建用户: N/n ---|')
        print('|--- 登录账户: E/e ---|')
        print('|--- 退出程序: Q/q ---|')
        strs = input('请输入指令代码：')
        if strs == 'N' or strs == 'n':
            name = input('请输入用户名：')
            register(name)
        elif strs == 'E' or strs == 'e':
            name = input('请输入用户名：')
            login(name)
        elif strs == 'Q' or strs == 'q':
            print('退出...')
            break
if __name__ == '__main__':
    user = {}
    main()