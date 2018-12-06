#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/19 15:59
# @Author : 小仙女
# @Site : 
# @File : 1.type().py
# @Software: PyCharm
class MyClass(object):
    def func(self,name):
        print(name)

myc = MyClass()

print(MyClass, type(MyClass))
print(myc, type(myc))
# 结果
# <class '__main__.MyClass'> <class 'type'>
# <__main__.MyClass object at 0x000001A4134C8160> <class '__main__.MyClass'>
# 我们创建了一个名为MyClass的类，并实例化了这个类，得到其对象myc
# type()函数可以查看一个类型或变量的类型，MyClass是一个class，它的类型就是type，而myc是一个实例，它的类型就是class MyClass。
#我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出MyClass类，而无需通过Class MyClass(object)...的定义：
#方式二
# 动态创建类
# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
def fn(self,name='world'):#先定义函数
    print('hello,%s'%name)

MyClass = type('MyClass',(object,),{'func':fn})#创建MyClass类,得到一个type的类对象
#MyClass = type('MyClass', (object,), {'func':lambda self,name:name}) # 创建MyClass类
myc = MyClass()
print(MyClass,type(MyClass))
print(myc,type(myc))
#要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名func上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# type就是创建类对象的类。你可以通过检查__class__属性来看到这一点。Python中所有的东西，注意，我是指所有的东西——都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类(元类，默认为type，也可以自定制)创建而来。type也是由type创建。。
'''
4.3  __metaclass__ 属性
'''
# class Foo(object):
#     __metaclass__ = something
