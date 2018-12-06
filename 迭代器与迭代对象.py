#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/9 15:15
# @Author : 小仙女
# @Site : 
# @File : 迭代器与迭代对象.py
# @Software: PyCharm
#1迭代
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable)) #列表是
print(isinstance('',Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance(1,Iterable))
#python中列表,元祖,字符串,字典都是可迭代对象,而整型数据不是可迭代对象
#可迭代对象的内部必须实现一个方法,__iter__()方法,这个方法的功能是,返回一个迭代器,这个迭代器是帮助自己进行迭代的.实现这个方法的对象,python就人为它是可迭代对象.调用了他们内部的__iter__方法，把他们变成了迭代器
#我们自己创建一个类,里面实现iter方法 python就人为它的对象是可迭代对象了
class MyIterableObj(object):
    def __iter__(self):
        pass
demo1 = MyIterableObj()
print(isinstance(demo1,Iterable)) #True
#迭代器的实质:
#迭代器遵循迭代器协议：必须拥有__iter__方法和__next__方法。
#__iter__() 功能是返回一个迭代器，帮助我们自己这种类型进行迭代，因为自己就是迭代器，所以迭代器中的__iter__() 返回的是self自己
#__next__() 功能是：  简单的说就是返回当前元素的，就像列表当中，取出第一个元素，再调用next的时候就取出了第二个元素。
# 但是在for循环当中放入列表的时候，for是怎么知道列表最后一个元素都已经取完了呢？？？？（我的天啊！不知道啊！！呜呜！！！）别着急，继续往下看复杂的说, next会做两件事：1 如果当前数据没有超出范围，这次当前值返回，然后自己进行标记，找到下一个要返回的值如果当前迭代器上次取出了最后一个元素，这一次当前数据是在范围之外的，那么就抛出异常(StopIteration)，告诉for循环等一些内建工具，迭代结束了。
print(isinstance([],Iterator))#False 很显然,可迭代对象不是迭代器
print(isinstance([].__iter__(),Iterator))# True 这是调用了可迭代对象的iter方法得到一个迭代器对象
#在python中内建了iter()方法和next()方法,把对象传进去与__iter__和__next__相同功能
print(isinstance(iter([]),Iterator))#True
#自己实现一个迭代器
class MyIterator(object):
    def __iter__(self):
        pass
    def __next__(self):
        pass
demo2 = MyIterator()
print(isinstance(demo2,Iterator))#True
#迭代器都是可迭代对象，因为迭代器一定有__iter__方法，所以它一定是迭代对象
'''
接下来,我们具体实现一个能够完成功能,能够放入for 循环遍历的迭代器
实现的业务是:传入一个参数n,我们要迭代出0到n的数'''
class NumIterator(object):
    #初始化我们接收 一个参数n,告诉我们迭代到多少结束
    def __init__(self,n):
        self.n = n
        #实际上是把i交给函数调用者
        self.i = 0
    #iter方法,返回一个迭代器,自己就是迭代器,所以返回自己
    def __iter__(self):
        return self
    #netx方法,判断是否越界,如果不越界返回一个元素,如果越界了抛出异常
    def __next__(self):
        #如果没有越界,我们返回给调用者迭代结果,如果越界了抛出异常
        if self.i <= self.n:
            res = self.i
            self.i +=1
            return res
        else:
            raise  StopIteration
#一个前三的自然数的迭代器对象
demo3 = NumIterator(3)
#调用python内建的next方法来获取迭代器的元素
print(next(demo3))
print(next(demo3))
print(next(demo3))
print(next(demo3))
#print(next(demo3))#抛出异常,越界了

demo4 = NumIterator(10)
for i in demo4:
    print(i)

'''
for 不知道我们放在in后面的是可迭代对象还是迭代器，他会先调用iter方法拿到一个迭代器，然后不停的调用next方法取到值，然后提供给我们，一直到取某个值的时候接收到了一个StopIteration异常，for循环就终止了。'''
