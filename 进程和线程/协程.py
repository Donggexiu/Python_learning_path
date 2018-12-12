#!/usr/bin/env/python
# _*_coding:utf-8_*_
# @Time : 2018/12/10 10:09
# @Author : Dxd
# @Site : 
# @File : 协程.py
# @Software: PyCharm
#yield当你调用这个函数的时候，你写在这个函数中的代码并没有真正的运行。这个函数仅仅只是返回一个生成器对象。
#yield结合装饰器（有返回值）
# def deco(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         next(res)
#         return res
#     return wrapper
#
# @deco
# def foo():
#     food_list = []
#     while True:
#         food= yield food_list#返回添加food的列表
#         food_list.append(food)
#         print('elements in foodlist are"',food)
#
# g = foo()
# print(g.send('苹果'))#低一次调用时,请使用next()语句,或者是send(None),不能使用send发送一个非None的值,因为没有python yield语句接收这个值
# print(g.send('梨子'))
# #send(msg) 和 next()是有返回值的，它们的返回值很特殊，返回的是下一个yield表达式的参数
# #基于yield并发执行
# import time
# def consumer():
#     '''任务1:接收数据,处理数据'''
#     while True:
#         x=yield
#         print("consumer拿到数据了x:",x)
#
# def producer():
#     '''任务2:生产数据'''
#     g=consumer()
#     next(g)
#     for i in range(10):
#         print("producer生产数据了",i)
#         g.send(i)
#
# start=time.time()
# #基于yield保存状态,实现两个任务直接来回切换,即并发的效果
# #PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
# producer()
#
# stop=time.time()
# print(stop-start)
# # yield不能实现io切换
# import time
# def consumer():
#     '''任务1:接收数据,处理数据'''
#     while True:
#         x=yield
#         print("consumer拿到数据了x:", x)
#
# def producer():
#     '''任务2:生产数据'''
#     g=consumer()
#     next(g)
#     for i in range(3):
#         print("producer生产数据了")
#         g.send(i)
#         time.sleep(2)
#
# start=time.time()
# producer() #并发执行,但是任务producer遇到io就会阻塞住,并不会切到该线程内的其他任务去执行
#
# stop=time.time()
# print(stop-start)
#协程的实现：
# yield返回
# send调用
# 协程的四个状态:
# inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
# GEN_CREATED：等待开始执行
# GEN_RUNNING：解释器正在执行
# GEN_SUSPENED：在yield表达式处暂停
# GEN_CLOSED：执行结束
# next预激（prime)
# 协程使用生成器函数定义：定义体中有yield关键字。
# def simple_coroutine():
#     print('Start')
#     x=yield
#     print('Received ',x)
# #主线程
# sc=simple_coroutine()#和创建生成器的方式一样，调用函数得到生成器对象
# print(111)
# #可以使用sc.send(None),效果一样
# next(sc)#这一步称为”预激“（prime）协程---即，让协程向前执行到第一个yield表达式，准备好作为活跃的协程使用。
# print(222)
# sc.send('Hello')
# 如果协程还未激活（GEN_CREATED 状态）要调用next(my_coro) 激活协程，也可以调用my_coro.send(None)
# 协程终止
# 协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）
# 止协程的一种方式：发送某个哨符值，让协程退出。内置的 None 和Ellipsis 等常量经常用作哨符值==。
# yield from
# 调用协程为了得到返回值，协程必须正常终止
# 生成器正常终止会发出StopIteration异常，异常对象的vlaue属性保存返回值
# yield from从内部捕获StopIteration异常
from gevent import monkey;

monkey.patch_all()

import gevent
import time


def eat():
    print('eat food 1')
    time.sleep(2)
    print('eat food 2')


def play_phone():
    print('play 1')
    time.sleep(1)
    print('play 2')


g1 = gevent.spawn(eat)
g2 = gevent.spawn(play_phone)
gevent.joinall([g1, g2])
print('主')
#五，Gevent之同步与异步
from gevent import spawn,joinall,monkey;monkey.patch_all()
import time
def task(pid):
    '''
    :param pid:
    :return:
    '''
    time.sleep(0.5)
    print('Task %s done'%pid)


def synchronous():
    for i in range(10):
        task(i)

def asynchronous():
    g_l=[spawn(task,i) for i in range(10)]
    joinall(g_l)

if __name__ == '__main__':
    print('synchronous')
    synchronous()
    print('asynchronous')
    asynchronous()##上面程序的重要部分是将task函数封装到Greenlet内部线程的gevent.spawn。初始化的greenlet列表存放在数组threads中，此数组被传给gevent.joinall 函数，后者阻塞当前流程，并执行所有给定的greenlet。执行流程只会在 所有greenlet执行完后才会继续向下走。