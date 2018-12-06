#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/16 16:25
# @Author : 小仙女
# @Site : 
# @File : 类的装饰器-有参数.py
# @Software: PyCharm
def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>', kwargs)
        return cls

    return decorate


@typeassert(name=str, age=int,
            salary=float)  # 有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
class People:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

p1 = People('egon', 18, 3333.3)
#刀光剑影
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        print('get--->', instance, owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->', instance, value)
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected %s' % str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('delete--->', instance)
        instance.__dict__.pop(self.name)


def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>', kwargs)
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


@typeassert(name=str, age=int,
            salary=float)  # 有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
class People:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


print(People.__dict__)
p1 = People('egon', 18, 3333.3)