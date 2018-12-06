#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/29 14:18
# @Author : 小仙女
# @Site : 
# @File : 知识储备.py
# @Software: PyCharm
'''exec():三个参数,参数1:字符串形式的命令.参数而.全局作用域(字典形式),如果不指定默认为globals(),参数三:局部作用域
如果不指定,默认为locals()'''
'__call__方法:对象后加括号,出发执行'
#eg: 对象=类名();而对于__call__方法执行的是由对象加括号出发的,即对象()或者类()
class Foo:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print('__call__')

f1 = Foo()#执行了__init__
f1()#执行__call__
#__call__的应用
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)

f2 = Foo()
f2(1,2,3,a=1,b=2)
#结果<__main__.Foo object at 0x000001AA838B71D0>
# (1, 2, 3)
# {'a': 1, 'b': 2}
'__new__方法:产生的新对象=object.__new__(继承object的子类)' \
'obj.__new__(cls)'
class Mymeta(type):
    def __init__(self,classname,class_bases,class_dic):
        if not classname.istitle():
            raise TypeError('类的首字母必须大写')
        if '__doc__' not in class_dic or class_dic['__doc__'].strip():
            raise TypeError('必须有注释,不能为空')
        super(Mymeta,self).__init__(classname,class_bases,class_dic)


class Chinese(object,metaclass=Mymeta):
    '''注释'''
    country = 'china'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking'%self.name)
# chinses = Mymeta(classname,c)

#自定义元类
def upper_attr_func(class_name,class_parents,class_attr):
    '''将属性名转为答谢会后,返回一个类对象'''
    #筛选出所有不以__开头的属性,转为大写
    upper_attr = {}
    for name ,value in class_attr.items():
        if not name.startswith('__'):
            upper_attr[name.upper()] = value

        else:
            upper_attr[name] = value


    return type(class_name,class_parents,upper_attr)

__metaclass__ = upper_attr_func#这将影响这个模块内的所有类。
class Foo():#虽然全局的 __metaclass__ 对 “object”无效
    bar = 'bip'
print(hasattr(Foo,'bar'))
print(hasattr(Foo,'Bar'))


