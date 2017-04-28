import easygui as g
strs = '''[ *真实姓名 ]为必填项。
[ *手机号码 ]为必填项。
[ *E-mail ]为必填项。'''
l1 = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
g.multenterbox(strs,'帐号中心',fields=l1)
