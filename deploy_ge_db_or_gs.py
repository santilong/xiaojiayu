#coding: utf-8
import pymysql
import paramiko
import threading
import sys, os, yagmail
def mysql(host, opt, dbname):
    conn = pymysql.connect(host, user='pymysql', passwd='pymysql', db=dbname)
    cur = conn.cursor()
    if 'update' or 'insert' or 'delete' in opt:
        try:
            cur.execute(opt)
            conn.commit()
        except:
            conn.rollback()
    else:
        cur.execute(opt)
    result = cur.fetchall()
    conn.close()
    print('SQL ' + opt + ' 执行输出结果为：')
    for re in result:
        print(re)
    print('\n')
    return result

def ssh(host, opt, dbname):
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(host, port=22, username='opsuser')
    stdin, stdout, stderr = s.exec_command(opt)
    stdoutInfo = stdout.readlines()
    stderrInfo = stderr.readlines()
    print(opt + '命令的执行输出为：')
    for out in stdoutInfo:
        print(out)
    print(opt + '命令的执行错误为：', stderrInfo, end='\n')
    s.close()
    return stdoutInfo

def thread(cmdict, func, dbname):
    threads = []
    for host,optlist in cmdict.items():
        for opt in optlist:
            t = threading.Thread(target=func, args=(host, opt, dbname))
            threads.append(t)
    for t in threads:
        try:
            t.start()
            t.join()
        except Exception as rs:
            print(rs)

def create_cmdict():
    ip = openfile()
    ip_list = []
    optlist = []
    cmdict = {}
    for each in ip:
        each = each.strip('\n')
        ip_list.append(each)
        while True:
            opt = input('请输入需要执行的命令：')
            if opt == '':
                break
            optlist.append(opt)
    cmdict = cmdict.fromkeys(ip_list, optlist)
    return cmdict

def openfile():
    with open(filename, 'r') as f:
        iplist = f.readlines()
    return iplist

def send_mail():
    msg = yagmail.yagmail.SMTP_SSL(user='请自行添加',password='请自行添加',host='smtp.gmail.com',port='465')
    msg.send(to='请自行添加'',subject='send mail test', contents=['hello world'],attachments='one.txt')

if __name__ == '__main__':
    option = sys.argv[1]
    filename = sys.argv[2]
    if os.path.splitext(filename)[0] == 'one':
        dbname = 'galaxy'
    else:
        dbname = 'galaxy_two'
    cmdict = create_cmdict()
    if option == 'mysql':
        thread(cmdict, mysql, dbname)
    elif option == 'command':
        thread(cmdict, ssh, dbname)
    send_mail()
