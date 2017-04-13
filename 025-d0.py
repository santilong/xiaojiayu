contact = {}
def search(name):
    if name in contact.keys():
        print(name + ':' +contact.get(name))
    else:
        print("没有该联系人！")

def insert(name):
    if name in contact.keys():
        print('您输入的姓名在通讯录中已存在' + '--->>' + name + ':' +contact[name])
        if input('是否修改用户资料(YES/No): ') == 'YES':
            number = input('请输入用户联系电话: ')
            contact[name] = number
    else:
        number = input('请输入用户联系电话: ')
        contact[name] = number

def delete(name):
    if name in contact.keys():
        contact.pop(name)
        print(name + '已经被删除!')
    else:
        print(name + '不存在!')

print("|--- 欢迎进入通讯程序 ---|")
print("|--- 1:查询联系人资料 ---|")
print("|--- 2:插入新的联系人 ---|")
print("|--- 3:删除已有联系人 ---|")
print("|--- 4:退出通讯录程序 ---|")

while True:
    chose =  input("请输入相关的指令代码：")
    if  chose == '1':
        name = input("请输入联系人姓名: ")
        search(name)
    elif chose == '2':
        name = input("请输入联系人姓名: ")
        insert(name)
    elif chose == '3':
        name = input("请输入联系人姓名: ")
        delete(name)
    elif chose == '4':
        break







