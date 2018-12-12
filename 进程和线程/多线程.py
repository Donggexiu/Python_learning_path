#!/usr/bin/env/python
# _*_coding:utf-8_*_
# @Time : 2018/12/7 16:25
# @Author : Dxd
# @Site : 
# @File : 多线程.py
# @Software: PyCharm
# GIL全局解释器锁
import queue
q = queue.Queue()
q.put('first')
q.put('second')
q.put('third')
print(q.get())
print(q.get())
print(q.get())

'''
结果(先进先出):
first
second
third
'''
#堆栈：last in fisrt out
q = queue.LifoQueue()
q.put('first')
q.put('second')
q.put('third')
print(q.get())
print(q.get())
print(q.get())
'''
结果(后进先出):
third
second
first
'''
# 优先级队列：存储数据时可设置优先级的队列
q = queue.PriorityQueue()
# put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((20, 'a'))
q.put((10, 'b'))
q.put((30, 'c'))
print(q.get())
print(q.get())
print(q.get())
'''
结果(数字越小优先级越高,优先级高的优先出队):
(10, 'b')
(20, 'a')
(30, 'c')
'''
#进程池与线程池
# concurrent.futures模块提供了高度封装的异步调用接口
# ThreadPoolExecutor：线程池，提供异步调用
# ProcessPoolExecutor: 进程池，提供异步调用
# submit(fn, *args, **kwargs)
# # 异步提交任务
# # map(func, *iterables, timeout=None, chunksize=1)
# # 取代for循环submit的操作
# # shutdown(wait=True)
# # 相当于进程池的pool.close() + pool.join()
# # 操作
# # wait = True，等待池内所有任务执行完毕回收完资源后才继续
# # wait = False，立即返回，并不会等待池内的任务执行完毕
# # 但不管wait参数为何值，整个程序都会等到所有任务执行完毕
# # submit和map必须在shutdown之前
# # result(timeout=None)
# # 取得结果
# # add_done_callback(fn)
# # 回调函数
#进程池
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import os,time,random
def task(n):
    print('%s is running'%n)
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=3)
    futures = []
    for i in range(11):
        future = executor.submit(task,i)
        futures.append(future)

    executor.shutdown(True)
    print('+++>')
    for future in futures:
        print(future.result())

#线程池


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)

    # for i in range(11):
    #     future=executor.submit(task,i)

    executor.map(task, range(1, 12))  # map取代了for+submit

#回调函数
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import requests
import json
import os


def get_page(url):
    print('<进程%s> get %s' % (os.getpid(), url))
    respone = requests.get(url)
    if respone.status_code == 200:
        return {'url': url, 'text': respone.text}


def parse_page(res):
    res = res.result()
    print('<进程%s> parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('db.txt', 'a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    p = ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)
# parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果