'''单线程'''
#coding: utf-8
# from time import ctime,sleep
# def music():
#     for i in range(2):
#         print('I was listening to music. %s' % ctime())
#         sleep(1)
# def movie():
#     for i in range(2):
#         print('I was watch the movies. %s' % ctime())
#         sleep(3)
# if __name__ == '__main__':
#     music()
#     movie()
#     print('all done at %s.' % ctime())

'''带入参数的单线程'''
# from time import ctime,sleep
# def music(arg):
#     for i in range(2):
#         print('I was listening to music %s at %s' % (arg,ctime()))
#         sleep(1)
# def movie(arg):
#     for i in range(2):
#         print('I was watch the movies %s at %s' % (arg,ctime()))
#         sleep(3)
# if __name__ == '__main__':
#     music('爱情买卖')
#     movie('日本裸体动作片')
#     print('all done at %s.' % ctime())

import threading
from time import ctime,sleep

def music(arg):
    for i in range(2):
        sleep(2)
        print('I was listening to music %s at %s' % (arg, ctime()))
def movie(arg):
    for i in range(2):
        sleep(3)
        print('I was watch the movies %s at %s' % (arg, ctime()))
threads = []
t1 = threading.Thread(target=music, args=['老司机'])
threads.append(t1)
t2 = threading.Thread(target=movie, args=['东京热'])
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    # t.join()
    print('all done at %s.' % ctime())