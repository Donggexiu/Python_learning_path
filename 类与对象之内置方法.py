#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/14 10:54
# @Author : 小仙女
# @Site : 
# @File : 类与对象之内置方法.py
# @Software: PyCharm
#1.1，isinstance(obj,cls)检查是否obj是否是类 cls 的对象
class Foo(object):
    pass
obj = Foo()
print(isinstance(obj,Foo))
#1.2，issubclass(sub, super)检查sub类是否是 super 类的派生类
class Foo(object):
    pass
class Bar(Foo):
    pass
print(issubclass(Bar, Foo))
'--反射--'
#反射，通过字符串映射到对象的属性首先这个例子，我们可以看出访问类或者对象的属性的时候，我们是对象.属性  类.属性
#所以实际上，点后面都是属性，而不是字符串，但是我们需要字符串'
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print('{} is talking'.format(self.name))

obj = People('tom',18)
print(obj.name)
print(obj.age)
'''通过字符串的形式操作对象相关的属性。python中的一切事物都是对象（都可以使用反射）'''
#2.1，hasattr(object,name) 判断object中有没有对应的方法和属性
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print('%s is talking'%self.name)
obj = People('huard',18)
print(hasattr(obj,'name'))
print(hasattr(obj,'talk'))
print(hasattr(obj,'age'))
#2.2，getattr(object, name, default=None)  获取object中有没有对应的方法和属性
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print('%s is talking'%self.name)
#def getattr(object, name, default=None): # known special case of getattr
    #
    # '''getattr(object, name[, default]) -> value'''
    # pass
obj = People('huard',18)
#如果有的话 就返回值，没有的话就返回None
print(getattr(obj,'name'))
print(getattr(obj,'talk'))
# print(getattr(obj,'age',default=None))
print(getattr(obj,'ads',None))
#2.3，setattr(x, y, v) 设置对象及其属性
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print('%s is talking'%self.name)
obj = People('huard',18)
setattr(obj,'sex','male')
print(obj.__dict__)
print(obj.sex)
#2.4，delattr(x, y) 删除类或对象的属性
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = People('huard', 18)
delattr(obj, 'age')
print(obj.__dict__)
#2.5，四个方法的使用演示
class BlackMedium:
    feature = 'Ugly'

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print('%s 黑中介卖房子啦,,但是谁能证明自己不mai' % self.name)

    def rent_house(self):
        print('%s 黑中介租房子啦,才租呢' % self.name)


b1 = BlackMedium('万成置地', '回龙观天露园')

# 检测是否含有某属性
print(hasattr(b1, 'name'))  # True
print(hasattr(b1, 'sell_house'))  # True

# 获取属性
n = getattr(b1, 'name')
print(n)  # 万成置地
func = getattr(b1, 'rent_house')
func()  # 万成置地 黑中介租房子啦,才租呢

# getattr(b1,'aaaaaaaa') #报错
'''    getattr(b1,'aaaaaaaa') #报错
AttributeError: 'BlackMedium' object has no attribute 'aaaaaaaa'
'''
# 为了不让报错，我们提前设置异常处理，如果没有的话 直接读取的是我们设置的
print(getattr(b1, 'aaaaaaaa', '不存在啊'))  # 不存在啊

# 设置属性
setattr(b1, 'sb', True)
setattr(b1, 'show_name', lambda self: self.name + 'sb')
print(b1.__dict__)
# {'name': '万成置地', 'addr': '回龙观天露园', 'sb': True, 'show_name': <function <lambda> at 0x000001A26A0E56A8>}
print(b1.show_name(b1))
# 万成置地sb

# 删除属性
delattr(b1, 'addr')
delattr(b1, 'show_name')
# delattr(b1,'show_name111')#不存在,则报错AttributeError: show_name111

print(b1.__dict__)  # {'name': '万成置地', 'sb': True}
#2.6，类也是对象
class Foo(object):
    staticField = "old boy"

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'
print(getattr(Foo, 'staticField'))
print(getattr(Foo, 'func'))
print(getattr(Foo, 'bar'))

#2.8，导入其他模块，利用反射查找该模块是否存在某个方法
# _*_ coding: utf-8 _*_
'''
module_test.py
def test():

    print('from the test')
import module_test as obj

#obj.test()

print(hasattr(obj,'test'))# True

getattr(obj,'test')()# from the test

'''
#反射的好处
#即你可以事先把主要的逻辑写好（只定义接口），然后后期再去实现接口的功能
#三 __setattr__,__delattr__,__getattr__
#3.1，三者的用法演示
class Foo:
    x = 1
    def __init__(self,y):
        self.y = y

    def __getattr__(self, item):
        print('--->from getattr: 你找的属性不存在')

    def __setattr__(self, key, value):
        print('--->from setattr')
        # self.key=value #这就无限递归了,你好好想想
        self.__dict__[key]=value #应该使用它

    def __delattr__(self, item):
        print('--->from delattr')
        #del self.item
        self.__dict__.pop(item)

#__setattr__添加修改属性会触发它的执行
f1 = Foo(100)
print(f1.__dict__)#因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,就是根本没赋值,除非你直接操作属性字典,否则永远无法赋值
f1.z = 3
print(f1.__dict__)
#__delattr 删除属性的时候会触发
f1.__dict__['a'] = 3#我们可以直接修改属性字典,来完成添加/修改属性的操作
del f1.a
print(f1.__dict__)
#__getattr__只有在使用点调用属性且属性不存在的时候才会出发
print(f1.xxxx)
#4.1，二次加工标准类型(基于继承实现)
class List(list):  # 继承list所有的属性，也可以派生出自己新的，比如append和mid
    def append(self, p_object):
        ' 派生自己的append：加上类型检查'
        if not isinstance(p_object, int):
            raise TypeError('must be int')
        super().append(p_object)

    @property
    def mid(self):
        '新增自己的属性'
        index = len(self) // 2
        return self[index]


l = List([1, 2, 3, 4])
print(l)
l.append(5)
print(l)
# l.append('1111111') #报错，必须为int类型

print(l.mid)

# 其余的方法都继承list的
l.insert(0, -123)
print(l)
l.clear()
print(l)
#
class List(list):
    def __init__(self,item,tag=False):
        super().__init__(item)
        self.tag=tag
    def append(self, p_object):
        if not isinstance(p_object,str):
            raise TypeError
        super().append(p_object)
    def clear(self):
        if not self.tag:
            raise PermissionError
        super().clear()


l = List([1, 2, 3], False)
print(l)
print(l.tag)

l.append('saf')
print(l)

# l.clear() #异常
l.tag = True
l.clear()