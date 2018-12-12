#!/usr/bin/env/python
# _*_coding:utf-8_*_
# @Time : 2018/12/7 9:47
# @Author : Dxd
# @Site : 
# @File : 多进程.py
# @Software: PyCharm
#多核cpupython使用多进程
#multiprocessing模块的功能众多：支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。需要再次强调的一点是：与线程不同，进程没有任何共享状态，进程修改的数据，改动仅限于该进程内。
# Process类的介绍
#Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，可用来开启一个子进程
# 强调：
# 1. 需要使用关键字的方式来指定参数
# 2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号
# group参数未使用，值始终为None
# target表示调用对象，即子进程要执行的任务
# args表示调用对象的位置参数元组，args=(1,2,'egon',)
# kwargs表示调用对象的字典,kwargs={'name':'egon','age':18}
# name为子进程的名称
# 方法介绍：
# p.start()：启动进程，并调用该子进程中的p.run()
# p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法
# p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，
# 使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
# p.is_alive():如果p仍然运行，返回True
# p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。
# timeout是可选的超时时间。
# 属性介绍：
# p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程
# 终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
# p.name:进程的名称
# p.pid：进程的pid
'创建并开启子进程的方式1'
import time
import random
# from multiprocessing import Process
# def piao(name):
#     print('%s is piaoying'%name)
#     time.sleep(random.randrange(1,5))
#     print('%s piao end'%name)
#
# if __name__ == '__main__':
#     p1 = Process(target=piao,args=('tom',))
#     p2 = Process(target=piao,args=('dxd',))
#     p3 = Process(target=piao, args=('wupeqi',))
#     p4 = Process(target=piao, args=('yuanhao',))
#     #调用对象下的方法,开启四个进程
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     print('主')
#创建并开启子进程的方式二
# import time
# import random
# from multiprocessing import Process
#
# class Piao(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         print('%s piaoing' %self.name)
#
#         time.sleep(random.randrange(1,5))
#         print('%s piao end' %self.name)
#
# if __name__ == '__main__':
#     #实例化得到四个对象
#     p1=Piao('egon')
#     p2=Piao('alex')
#     p3=Piao('wupeiqi')
#     p4=Piao('yuanhao')
#
#     #调用对象下的方法，开启四个进程
#     p1.start() #start会自动调用run
#     p2.start()
#     p3.start()
#     p4.start()
#     print('主')
#我们来测试一下（创建完子进程后，主进程所在的这个脚本就退出了，当父进程先于子进程结束时，子进程会被init收养，成为孤儿进程，而非僵尸进程），文件内容
# import os
# import sys
# import time
# pid = os.getpid()
# ppid = os.getpid()
# print('im father','pid',pid,'ppid',ppid)
# pid = os.fork() '-->linux下运行这一段代码'
# #执行pid=os.fork()则会生成一个子进程
# #返回值pid有两种:
# #    如果返回的pid值为0，表示在子进程当中
# #    如果返回的pid值>0，表示在父进程当中
# if pid >0:
#     print('father died')
#     sys.exit(0)
# #保证主线程退出完毕
# time.sleep(1)
# print("i'm  child",os.getpid(),os.getppid() )
'''
僵尸进程危害场景：
例如有个进程，它定期的产 生一个子进程，这个子进程需要做的事情很少，做完它该做的事情之后就退出了，因此这个子进程的生命周期很短，但是，父进程只管生成新的子进程，至于子进程 退出之后的事情，则一概不闻不问，这样，系统运行上一段时间之后，系统中就会存在很多的僵死进程，倘若用ps命令查看的话，就会看到很多状态为Z的进程。 严格地来说，僵死进程并不是问题的根源，罪魁祸首是产生出大量僵死进程的那个父进程。因此，当我们寻求如何消灭系统中大量的僵死进程时，答案就是把产生大 量僵死进程的那个元凶枪毙掉（也就是通过kill发送SIGTERM或者SIGKILL信号啦）。枪毙了元凶进程之后，它产生的僵死进程就变成了孤儿进 程，这些孤儿进程会被init进程接管，init进程会wait()这些孤儿进程，释放它们占用的系统进程表中的资源，这样，这些已经僵死的孤儿进程 就能瞑目而去了。
'''
# from multiprocessing import Process
# import time, os
#
#
# def run():
#     print('子', os.getpid())
#
#
# if __name__ == '__main__':
#     p = Process(target=run)
#     p.start()
#
#     print('主', os.getpid())
#     time.sleep(1000)
# Process对象的join方法
# 在主进程运行过程中如果想要并发的执行其他任务，我们可以开启子进程，此时主进程的任务和子进程的任务分为两种情况
# 一种情况是：在主进程的任务与子进程的任务彼此独立的情况下，主进程的任务先执行完毕后，主进程还需要等待子进程执行完毕，然后统一回收资源
# 一种情况是：如果主进程的任务在执行到某一个阶段时，需要等待子进程执行完毕后才能继续执行，就需要一种机制能够让主进程监测子进程是否运行完毕，在子进程执行完毕后才继续执行，否则一直在原地阻塞，这就是join方法的作用。
from  multiprocessing import Process
import time,os

def task(name):
    print("%s is running ,parent is %s"%(name,os.getppid()))
    time.sleep(1)


if __name__ == '__main__':

    p1 = Process(target=task,args=('子进程1',))
    # print(p1.is_alive())
    p2 = Process(target=task, args=('子进程2',))
    p3 = Process(target=task, args=('子进程3',))
    # print(p1.is_alive())
    p1.start()
    print(p1.is_alive())
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(p1.is_alive())
    print("主进程   %s is running ,parent is %s" % (os.getpid(), os.getppid()))
    print(p1.name)
#进程只要start就会在开始运行了,所以p1-p4.start()时,系统中已经有四个并发的进程了
# 而我们p1.join()是在等p1结束,没错p1只要不结束主线程就会一直卡在原地,这也是问题的关键
# join是让主线程等,而p1-p4仍然是并发执行的,p1.join的时候,其余p2,p3,p4仍然在运行,等#p1.join结束,可能p2,p3,p4早已经结束了,这样p2.join,p3.join.p4.join直接通过检测，无需等待
# 所以4个join花费的总时间仍然是耗费时间最长的那个进程运行的时间
'五'
# Process对象的其他属性或方法
from multiprocessing import Process
import time
import random

def task(name):
    print('%s is piaoing' %name)
    time.sleep(random.randrange(1,5))
    print('%s is piao end' %name)

if __name__ == '__main__':
    p1=Process(target=task,args=('egon',))
    p1.start()

    p1.terminate()#关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
    print(p1.is_alive()) #结果为True

    print('主')
    print(p1.is_alive()) #结果为False

# 进程对象的其他属性：name与pid

from multiprocessing import Process
import time
import random


def task(name):
    print('%s is piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s is piao end' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('egon',), name='子进程1')  # 可以用关键参数来指定进程名
    p1.start()

    print(p1.name, p1.pid, )

# 六守护进程
# 主进程创建子进程，然后将该进程设置成守护自己的进程，守护进程就好比崇祯皇帝身边的老太监，崇祯皇帝已死老太监就跟着殉葬了。
# 关于守护进程需要强调两点：
# ：守护进程会在主进程代码执行结束后就终止
# 其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
# 如果我们有两个任务需要并发执行，那么开一个主进程和一个子进程分别去执行就ok了，如果子进程的任务在主进程任务结束后就没有存在的必要了，那么该子进程应该在开启前就被设置成守护进程。主进程代码运行结束，守护进程随即终止
from multiprocessing import Process
import time
import random

def task(name):
    print('%s is piaoing' %name)
    time.sleep(random.randrange(1,3))
    print('%s is piao end' %name)


if __name__ == '__main__':
    p=Process(target=task,args=('egon',))
    p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()
    print('主') #只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了

from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")


# 基于多线程实现的并发套接字通信
# import socket
#
# ip_port = ('127.0.0.1',9099)
# client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(ip_port)
# while True:
#     try:
#         msg = input('请输入>>>:').strip()
#         data = client.send(msg.encode('utf-8'))
#         if not data:break
#
#     except ConnectionResetError:break
#
#     recv_data = client.recv(1024)
#     print(recv_data)
# client.close()
#
# #服务端
# from multiprocessing import Process
#
# def talk(conn):
#     while True:
#         try:
#             data = conn.recv(1024)
#             if not data :
#                 break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#     conn.close()
#
# def server(ip_port):
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server.bind(ip_port)
#     server.listen(5)
#     while True:
#         conn, addr = server.accept()
#         p =Process(target=talk,args=(conn,))
#         p.start()
#     server.close()
#
# if __name__ == '__main__':
#     ip_port = ('127.0.0.1', 9999)
#     print('启动')
#     server(ip_port)


# 队列
# 进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的
# 创建队列的类（底层就是以管道和锁定的方式实现）：
# Queue([maxsize]):创建共享的进程队列,Queue是进程安全的队列,可以使用Queue实现多进程之间的数据传递
# maxsize是队列中允许最大项数，省略则无大小限制。
# 但需要明确：
# 队列内存放的是消息而非大数据
# 队列占用的是内存空间，因而maxsize即便是无大小限制也受限于内存大小
#主要方法介绍:
# q.put方法用以插入数据到队列中。
# q.get方法可以从队列读取并且删除一个元素。
'队列的使用'
from multiprocessing import Process,Queue
q = Queue(3)
#put ,get ,put_nowait,get_nowait,full,empty
q.put(1)
q.put(2)
q.put(3)
print(q.full())#满了
#q.put(4)再放就阻塞住了
print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了
# print(q.get()) #再取就阻塞住了