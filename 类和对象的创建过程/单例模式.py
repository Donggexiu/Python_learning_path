#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/19 17:57
# @Author : 小仙女
# @Site : 
# @File : 单例模式.py
# @Software: PyCharm
'''
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。
在 Python 中，我们可以用多种方法来实现单例模式
'''
'1.使用模块'
# 其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：
# mysingleton.py
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
# from a import singleton
'2.使用装饰器'
def singleton(cls):
    _instance = {}
    def _singleton(*args,**kwargs):
        if cls not  in _instance:
            _instance[cls] = cls(*args)
        return _instance[cls]
    return _singleton
@singleton
class A(object):
    a = 1

    def __init__(self,x = 0):
        self.x = x

a1 = A(2)
a2 = A(3)
#3.使用类

class Singleton(object):
    def __init__(self):
        import time
        time.sleep(1)
    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(singleton,'_instance'):
            Singleton._instance = Singleton(*args,**kwargs)

        return Singleton._instance
#一般情况，大家以为这样就完成了单例模式，但是这样当使用多线程时会存在问题
import threading
def task(arg):
    obj = Singleton.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
# 看起来也没有问题，那是因为执行速度过快，如果在init方法中有一些IO操作，就会发现问题了，下面我们通过time.sleep模拟
# 4.基于__new__方法实现（推荐使用，方便）
# 我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式
import threading
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
#5.基于metaclass方式实现
"""
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

obj = Foo()
# 执行type的 __call__ 方法，调用 Foo类（是type的对象）的 __new__方法，用于创建对象，然后调用 Foo类（是type的对象）的 __init__方法，用于对对象初始化。

obj()    # 执行Foo的 __call__ 方法
