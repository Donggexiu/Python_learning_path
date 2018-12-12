#!/usr/bin/env/python
# _*_coding:utf-8_*_
# @Time : 2018/12/7 11:53
# @Author : Dxd
# @Site : 
# @File : 练习题.py
# @Software: PyCharm
# 练习题：改写下面程序，分别实现下述打印效果
from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)

if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    p1.start()
    p2.start()
    p3.start()

    print('-------->4')
# 效果一：保证最先输出-------->4
#
# -------->4
# -------->1
# -------->3
# -------->2
# 　　程序：不用修改
from multiprocessing import Process
import time
import random


def task(n):
    time.sleep(random.randint(1, 2))
    print("---------->%s" % n)


if __name__ == '__main__':
    p1 = Process(target=task, args=(1,))
    p2 = Process(target=task, args=(2,))
    p3 = Process(target=task, args=(3,))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()


    print("---------->4")
#
# 　　
#
# 效果二：保证最后输出 - ------->4
#
# -------->2
# -------->3
# -------->1
# -------->4