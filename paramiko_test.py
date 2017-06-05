# import paramiko
# def paramiko_cmd(host='52.32.118.25', port=22, user='opsuser', opt='df -h'):
#     # paramiko.util.log_to_file('paramiko.log')
#     # s = paramiko.SSHClient()
#     s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     s.conect(host, port, user)
#     stdin, stdout, stderr = s.exec_command(opt)
#     stdoutInfo = stdout.readlines()
#     stderrInfo = stderr.readlines()
#     return stdoutInfo
#
# paramiko_cmd()