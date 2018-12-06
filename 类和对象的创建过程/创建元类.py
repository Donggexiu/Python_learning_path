#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/30 13:34
# @Author : 小仙女
# @Site : 
# @File : 创建元类.py
# @Software: PyCharm
#type事实上跟str和int类似的类,所以能继承他

class UpperAttrMetaclass(type):
    '''
    __new__方法在__init__之前执行,这个方法创建对象并返回
    __init__方法仅仅初始化做为参数传入的对象
    __new__很少使用__new__方法,除非你想控制类是如何创建的
    这里创建的对象是一个类,我们想自定义它,因此需要覆盖__new__
    一些高级用法还包括覆盖__call__方法,这里使用
    '''
    def __new__(upperattr_metaclass,future_class_name,class_parents,class_attr):
        uppercase_attr = {}
        for name,value in class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = value

            else:
                uppercase_attr[name] = value

        #return type(future_class_name,class_parents,uppercase_attr)事实上这不是opp 直接调用了type函数,没有覆盖或者调用父类的__new__,
        return type.__new__(upperattr_metaclass, future_class_name,
                            class_parents, uppercase_attr)
    '额外的参数upperattr_metaclass，这没什么特别的：__new__方法总是接受定义的类作为第一个参数，就像普通方法接受实例作为第一个参数传入self，类方法传入定义类一样'
#因此一个真实的正式的metaclass应该像这样写：
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        #return type.__new__(cls, clsname, bases, uppercase_attr)
        #我们使用super让代码看上去更清晰一些，
        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)




