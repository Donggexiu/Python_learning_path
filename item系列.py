#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/19 13:44
# @Author : 小仙女
# @Site : 
# @File : item系列.py
# @Software: PyCharm
'''
__getitem__\__setitem__\__delitem__
我们在列表中学过这种取元素的方式。比如说lst = [1,2,3,4],取第一个元素 lst[0],又或者在字典中dd ={'name':'xiaohua'} 取元素dd['name']。实际上，这种取元素的方式，与__getitem__,__setitem__,__delitem__三个函数有关。
下面，我们一一来看看上述三个函数的用法：
__getitem__：当我们想要按照 obj[attr]方式调用对象的属性时，触发这个函数的执行
'''
#__getitem__：当我们想要按照 obj[attr]方式调用对象的属性时，触发这个函数的执行
class Foo:
    def __init__(self,name):
        self.name = name
    def __getitem__(self, item):
        print('我执行了')

f = Foo('alex')
print(f.__dict__) # 对象的名称空间只有一个属性
f['name']  # 触发getitem执行

#####输出结果########
# {'name': 'alex'}
# 我执行了
#从上面结果，可以看出，当我试图以f['name']方式调用属性的时候，就会触发__getitem__执行。一般将__getitem__设置为如下：
class Foo:
    def __init__(self,name):
        self.name = name
    def __getitem__(self, item):
            print(self.__dict__[item])

f = Foo('alex')
print(f.__dict__)
f['name']
########输出结果#######
'''{'name': 'alex'}
alex'''
#__setitem__：当我以f['name'] = 'xiaohua' 方式修改对象属性值的时候，会触发该函数的执行。
class Foo:
    def __init__(self,name):
        self.name = name

    def __setitem__(self, key, value):
        print('setitem')

f = Foo('alex')
print(f.__dict__)
f['x'] = 3
print(f.__dict__)
#一般将setitem设置为如下，当然你也可以按照自己的方式进行设置。
class Foo:
    def __init__(self,name):
        self.name = name

    def __setitem__(self, key, value):
        print('我执行了')
        self.__dict__[key] = value

f2 = Foo('alan')
print(f2.__dict__)
f2['y'] = 4
print(f2.__dict__)
#__delitem__：当以del f['name'] 方式删除对象的属性值时，会触发這个函数的执行
class Foo:
    def __init__(self,name):
        self.name = name

    def __delitem__(self, key):
        print('我执行了')

f = Foo('alex')
print(f.__dict__)
del f['name']#出发delitem执行
####输出结果#####
# {'name': 'alex'}
# 我执行了
#一般设置为如下方式：
class Foo:
    def __init__(self,name):
        self.name = name

    def __delitem__(self, key):
        del f.__dict__[key]


f = Foo('alex')
print(f.__dict__)
del f['name']
print(f.__dict__)
#########输出结果####
# {'name': 'alex'}
# {}

