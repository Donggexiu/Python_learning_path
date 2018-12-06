#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/14 10:07
# @Author : 小仙女
# @Site : 
# @File : 类与对象练习.py
# @Software: PyCharm
import uuid
import pickle
import os
'''
uuid模块
UUID主要有五个算法，也就是五种方法来实现：
 1、uuid1()——基于时间戳
 由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）
 算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
实际中很少用到该方法。
3、uuid3()——基于名字的MD5散列值
 通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
  和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。   
 4、uuid4()——基于随机数
 由伪随机数得到，有一定的重复概率，该概率可以计算出来。
  5、uuid5()——基于名字的SHA-1散列值
 算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法'''
class Mysql(object):
    def __init__(self,host,port):
        self.id =self.create_id()
        self.host = host
        self.port = port
    def save(self):
        pass
    @property
    def is_exists(self):
        pass
    @staticmethod
    def get_obj_by_id(id):
        pass
    @staticmethod
    def create_id():
        return str(uuid.uuid1())

import time
class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():#用Date.now()的形式去产生实例,该实例用的是当前时间
        t =time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    @staticmethod
    def tomorrow():#用Date.tomorrow()的形式与产生实例,该实例用的是明天的时间
        t = time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

a = Date('1994',12,21)
b = Date.now()
c = Date.tomorrow()
print(a.year,b.year,c.year)
print(a.month,b.month,c.month)
print(a.day,b.day,c.day)
#-----分割线
class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod
    def now():
        t=time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)

e=EuroDate.now()
print(e)#我们的意图是想触发EuroDate.__str__,但是结果为
#因为e就是用Date类产生的,所以根本不会触发EuroDate.__str__,解决方法就是用classmethod
class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def now(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)#哪个类来调用,即用哪个类cls来实例化

class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)

e=EuroDate.now()
print(e)#我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿