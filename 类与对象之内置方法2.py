#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/14 16:07
# @Author : 小仙女
# @Site : 
# @File : 类与对象之内置方法2.py
# @Software: PyCharm
from configobj import ConfigObj
'''
六 描述符(__get__,__set__,__delete__)
1 描述符是什么:描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()中的一个,这也被称为描述符协议
__get__():调用一个属性时,触发
__set__():为一个属性赋值时,触发
__delete__():采用del删除属性时,触发
'''
class Foo: #在python3中Foo是新式类,它实现了三种方法,这个类就被称作一个描述符
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
#2 描述符是干什么的:描述符的作用是用来代理另外一个类的属性的(必须把描述符定义成这个类的类属性，不能定义到构造函数中)
#引子:描述符类产生的实例进行属性操作并不会触发三个方法的执行
class Foo(object):
    def __get__(self, instance, owner):
        print('触发get')
    def __set__(self, instance, value):
        print('触发set')

    def __delete__(self, instance):
        print('触发delete')
##包含这三个方法的新式类称为描述符,由这个类产生的实例进行属性的调用/赋值/删除,并不会触发这三个方法
f1 = Foo()
f1.name = 'tom'
print(f1.name)
del f1.name#疑问:何时,何地,会触发这三个方法的执行
#1，描述符应用之何时?何地?
class Str:
    def __get__(self, instance, owner):
        print('str调用')
    def __set__(self, instance, value):
        print('str设置')
    def __delete__(self, instance):
        print('str删除')

#描述符int
class Int:
    def __get__(self, instance, owner):
        print('Int调用')
    def __set__(self, instance, value):
        print('Int设置...')
    def __delete__(self, instance):
        print('Int删除...')
class People:
    name=Str()
    age=Int()
    def __init__(self,name,age): #name被Str类代理,age被Int类代理,
        self.name=name
        self.age=age

#何地？：定义成另外一个类的类属性

p1 = People('TOM',18)
print(p1.name)
p1.name = 'xiaohong'
del p1.name
p1.age = 18
del p1.age
print(p1.__dict__)
print(People.__dict__)
#补充
print(type(p1) == People)#type(obj)其实是查看obj是由哪个类实例化来的
print(type(p1).__dict__ == People.__dict__)
#类属性>数据描述符
# 描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')

    def __set__(self, instance, value):
        print('Str设置...')

    def __delete__(self, instance):
        print('Str删除...')


class People:
    name = Str()

    def __init__(self, name, age):  # name被Str类代理,age被Int类代理,
        self.name = name
        self.age = age

'''
2，描述符分两种 一 数据描述符:至少实现了__get__()和__set__()
class Foo:
    def __set__(self, instance, value):
        print('set')
    def __get__(self, instance, owner):
        print('get')

二 非数据描述符:没有实现__set__()

class Foo:
    def __get__(self, instance, owner):
        print('get')
'''
# 一 描述符本身应该定义成新式类,被代理的类也应该是新式类
# 二 必须把描述符定义成这个类的类属性，不能为定义到构造函数中
# 三 要严格遵循该优先级,优先级由高到底分别是
# 类属性
# 数据描述符
# 实例属性
# 非数据描述符
# 找不到的属性触发__getattr__()
# 基于上面的演示,我们已经知道,在一个类中定义描述符它就是一个类属性,
#存在于类的属性字典中, 而不是实例的属性字典

# 那既然描述符被定义成了一个类属性,直接通过类名也一定可以调用吧,没错
People.name  # 恩,调用类属性name,本质就是在调用描述符Str,触发了__get__()

People.name = 'egon'  # 那赋值呢,我去,并没有触发__set__()
del People.name  # 赶紧试试del,我去,也没有触发__delete__()
# 结论:描述符对类没有作用-------->傻逼到家的结论
'''
原因:描述符在使用时被定义成另外一个类的类属性,因而类属性比二次加工的描述符
伪装而来的类属性有更高的优先级
People.name #恩,调用类属性name,找不到就去找描述符伪装的类属性name,触发了__get__()
People.name='egon' #那赋值呢,直接赋值了一个类属性,它拥有更高的优先级,
相当于覆盖了描述符,肯定不会触发描述符的__set__()
del People.name #同上'''
#数据描述符>实例属性
# 描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')

    def __set__(self, instance, value):
        print('Str设置...')

    def __delete__(self, instance):
        print('Str删除...')


class People:
    name = Str()

    def __init__(self, name, age):  # name被Str类代理,age被Int类代理,
        self.name = name
        self.age = age


p1 = People('egon', 18)

# 如果描述符是一个数据描述符(即有__get__又有__set__),那么p1.name的调
#用与赋值都是触发描述符的操作, 于p1本身无关了, 相当于覆盖了实例的属性
p1.name = 'egonnnnnn'
p1.name
print(p1.__dict__)  # 实例的属性字典中没有name,因为name是一个数据描述符,
#优先级高于实例属性, 查看 / 赋值 / 删除都是跟描述符有关, 与实例无关了
del p1.name
#实例属性>非数据描述符
class Foo:
    def func(self):
        print('我胡汉三又回来了')
f1 = Foo()
f1.func()  # 调用类的方法,也可以说是调用非数据描述符
# 函数是一个非数据描述符对象(一切皆对象么)
print(dir(Foo.func))
print(hasattr(Foo.func, '__set__'))
print(hasattr(Foo.func, '__get__'))
print(hasattr(Foo.func, '__delete__'))
# 有人可能会问,描述符不都是类么,函数怎么算也应该是一个对象啊,怎么就是描述符了
# 笨蛋哥,描述符是类没问题,描述符在应用的时候不都是实例化成一个类属性么
# 函数就是一个由非描述符类实例化得到的对象
# 没错，字符串也一样
f1.func = '这是实例属性啊'
print(f1.func)

del f1.func  # 删掉了非数据
f1.func()
#实例属性>非数据描述符
class Foo:
    def __set__(self, instance, value):
        print('set')

    def __get__(self, instance, owner):
        print('get')


class Room:
    name = Foo()

    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length


# name是一个数据描述符,因为name=Foo()而Foo实现了get和set方法,因而比实例属性有更高的优先级
# 对实例的属性操作,触发的都是描述符的
r1 = Room('厕所', 1, 1)
r1.name
r1.name = '厨房'


class Foo:
    def __get__(self, instance, owner):
        print('get')


class Room:
    name = Foo()

    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length


# name是一个非数据描述符,因为name=Foo()而Foo没有实现set方法,因而比实例属性有更低的优先级
# 对实例的属性操作,触发的都是实例自己的
r1 = Room('厕所', 1, 1)
r1.name
r1.name = '厨房'
#5 描述符使用
class Str:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print('get--->', instance, owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->', instance, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('delete--->', instance)
        instance.__dict__.pop(self.name)


class People:
    name = Str('name')

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People('egon', 18, 3231.3)

# 调用
print(p1.__dict__)
p1.name

# 赋值
print(p1.__dict__)
p1.name = 'egonlin'
print(p1.__dict__)

# 删除
print(p1.__dict__)
del p1.name
print(p1.__dict__)
#拔刀相助
class Str:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print('get--->', instance, owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->', instance, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('delete--->', instance)
        instance.__dict__.pop(self.name)


class People:
    name = Str('name')

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# 疑问:如果我用类名去操作属性呢
People.name  # 报错,错误的根源在于类去操作属性时,会把None传给instance


# 修订__get__方法
class Str:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print('get--->', instance, owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->', instance, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('delete--->', instance)
        instance.__dict__.pop(self.name)


class People:
    name = Str('name')

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


print(People.name)  # 完美,解决
#磨刀霍霍
class Str:
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
        if not isinstance(value, self.expected_type):  # 如果不是期望的类型，则抛出异常
            raise TypeError('Expected %s' % str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('delete--->', instance)
        instance.__dict__.pop(self.name)


class People:
    name = Str('name', str)  # 新增类型限制str

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People(123, 18, 3333.3)  # 传入的name因不是字符串类型而抛出异常


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


class People:
    name = Typed('name', str)
    age = Typed('name', int)
    salary = Typed('name', float)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People(123, 18, 3333.3)
p1 = People('egon', '18', 3333.3)
p1 = People('egon', 18, 3333)
#类的装饰器:无参
def decorate(cls):
    print('类的装饰器开始运行啦------>')
    return cls


@decorate  # 无参:People=decorate(People)
class People:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People('egon', 18, 3333.3)