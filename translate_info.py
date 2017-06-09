#coding: utf-8
'''直接转换运营给的信息:'''
import paramiko

listInfo = [
["World1349","World1350","World1351","World1352","World1353","World1354","World1355","World1356","World1357","World1358","World1359",],

["World1360","World1361","World1362","World1363","World1364","World1365","World1366","World1367","World1368","World1369",],

["World1370","World1371","World1372","World1373","World1374","World1375","World1376","World1377",],

["World1455","World1456","World1457","World1458","World1459","World1460","World1461","World1462","World1463",],

["World1464","World1465","World1466","World1467","World1468","World1469","World1470","World1471","World1472",],

["World1473","World1474","World1475","World1476","World1477",],
]

def ssh2(relayip,opt):
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=relayip, port=22, username='opsuser')
        stdin, stdout, stderr = s.exec_command(opt)
        stdoutInfo = stdout.readlines()
        stderrInof = stderr.readlines()
        print opt + '执行结果如下：\n'
        for each in stdoutInfo:
            print '\033[32m %s \033[0m' % each
        print opt + '执行报错如下：\n'
        for each in stderrInof:
            print '\033[31m' + each + '\033[0m'
    except Exception as reason:
        print reason
    return stdoutInfo

def sqlstatment():
    optlist1 = []
    optlist2 = []
    tranall = []
    length = len(listInfo)
    print '一共' + str(length) + '条逻辑服信息:\n'
    for each in range(0,length):
        tranlist = 'select name,ip,port,is_in_maintain,status,node_name,logic_id,public_ip from servers where name in' + str(tuple((listInfo[each]))) + ';'
        optlist1.append(tranlist)
    for each1 in listInfo:
        for each2 in each1:
            tranall.append(each2)
    tranall = 'select name,ip,port,is_in_maintain,status,node_name,logic_id,public_ip from servers where name in' + str(tuple(tranall)) + ';'
    optlist1.append(tranall)
    opt = 'mysql -u' + dbuser + ' ' + '-p' + dbpwd + ' ' + '-h' + gwip + ' ' + dbname + ' ' + '-e'
    for each in optlist1:
        optlist2.append(opt + ' ' + '"' + each + '"')
    return optlist2

def main():
    for opt in sql:
        ssh2(relayip,opt)

if __name__ == '__main__':
    dbuser = 'migratdb'
    dbpwd = 'migratdb^*^'
    gwip = '10.0.163.200'
    dbname = 'galaxy_legend_ucenter'
    relayip = '52.10.161.92'
    sql = sqlstatment()
    main()