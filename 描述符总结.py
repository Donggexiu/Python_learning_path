#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/19 10:14
# @Author : 小仙女
# @Site : 
# @File : 描述符总结.py
# @Software: PyCharm
'''
6 描述符总结
描述符是可以实现大部分python类特性中的底层魔法,包括@classmethod,@staticmethd,@property甚至是__slots__属性
描述父是很多高级库和框架的重要工具之一,描述符通常是使用到装饰器或者元类的大型框架中的一个组件.
7 利用描述符原理完成一个自定制@property,实现延迟计算（本质就是把一个函数属性利用装饰器原理做成一个描述符：类的属性字典中函数名为key，value为描述符类产生的对象）
'''
#@property
class Room:
    def __init__(self,name,width,length):
        self.name = name
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width*self.length

r1 = Room('alex',1,1)
print(r1.area)
#自己做一个@property
class Lazyproperty:
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        print('这是自己定制的静态属性,r1.area实际是要执行r1.area()')
        if instance is None:
            return self
        return self.func(instance)#此时你应该明白,到底是谁在为你做自动传递self的事情

class Room:
    def __init__(self,name,width,length):
        self.name = name
        self.width = width
        self.length = length

    @Lazyproperty #area = Lazyproperty(area) 相当于定义了一个类属性,即描述符
    def area(self):
        return self.width*self.length

r1 = Room('alex',1,1)
print(r1.area)
#自己做一个@classmethod
class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):  # 类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback():
            print('在这里可以加功能啊...')
            return self.func(owner)

        return feedback


class People:
    name = 'linhaifeng'

    @ClassMethod  # say_hi=ClassMethod(say_hi)
    def say_hi(cls):
        print('你好啊,帅哥 %s' % cls.name)


People.say_hi()

p1 = People()
p1.say_hi()
# 疑问,类方法如果有参数呢,好说,好说
class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):  # 类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args, **kwargs):
            print('在这里可以加功能啊...')
            return self.func(owner, *args, **kwargs)

        return feedback


class People:
    name = 'linhaifeng'

    @ClassMethod  # say_hi=ClassMethod(say_hi)
    def say_hi(cls, msg):
        print('你好啊,帅哥 %s %s' % (cls.name, msg))


People.say_hi('你是那偷心的贼')

p1 = People()
p1.say_hi('你是那偷心的贼')

#9 利用描述符原理完成一个自定制的@staticmethod

#自己做一个@staticmethod

class StaticMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args,**kwargs):
            print('在这里可以加功能啊...')
            return self.func(*args,**kwargs)
        return feedback

class People:
    @StaticMethod# say_hi=StaticMethod(say_hi)
    def say_hi(x,y,z):
        print('------>',x,y,z)

People.say_hi(1,2,3)

p1=People()
p1.say_hi(4,5,6)
#再看property
#一个静态属性property本质就是实现了get，set，delete三种方法
class Foo:
    @property
    def AAA(self):
        print('get的时候运行我')

    @AAA.setter
    def AAA(self,value):
        print('set 的时候运行我')

    @AAA.deleter
    def AAA(self):
        print('delete的时候运行我')

#只有在属性AAA定义property后才能AAA.setter,AAA.deleter
f1 = Foo()
f1.AAA
f1.AAA = 'aaa'
del f1.AAA
#第二种
class Foo:
    def get_AAA(self):
        print('get的时候运行我啊')

    def set_AAA(self, value):
        print('set的时候运行我啊')

    def delete_AAA(self):
        print('delete的时候运行我啊')

    AAA = property(get_AAA, set_AAA, delete_AAA)  # 内置property三个参数与get,set,delete一一对应

f2 = Foo()
f2.AAA
f2.AAA = 'bbb'
del f2.AAA

'''怎么用'''
##实现类型检测功能
class People:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.name

#p1 = People('alex')#property自动实现了set和get方法属于数据描述符,比实例属性优先级高,所以你这面写会触发property内置的set,抛出异常

#修订
class People:
    def __init__(self, name):
        self.name = name  # 实例化就触发property

    @property
    def name(self):
        # return self.name #无限递归
        print('get------>')
        return self.Douniwan
    @name.setter
    def name(self,value):
        print('set------')
        self.Douniwan = value

    @name.deleter
    def name(self):
        print('delete------>')
        del self.Douniwan


p1 = People('alex')#self.name实际是存放到self.DouNiWan里
print(p1.name)
print(p1.name)
print(p1.name)
print(p1.__dict__)
p1.name='egon'
print(p1.__dict__)
del p1.name
print(p1.__dict__)
#第三关:加上类型检查
class People:
    def __init__(self, name):
        self.name = name  # 实例化就触发property

    @property
    def name(self):
        # return self.name #无限递归
        print('get------>')
        return self.DouNiWan
    @name.setter
    def name(self,value):
        print('set ----->')
        if not isinstance(value,str):
            raise TypeError("必须是字符串")
        self.DouNiWan = value

    @name.deleter
    def name(self):
        print('delete------>')
        del self.DouNiWan

p1=People('alex') #self.name实际是存放到self.DouNiWan里
p1.name=1
