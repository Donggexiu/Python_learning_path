#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/13 10:09
# @Author : 小仙女
# @Site : 
# @File : 类与继承.py
# @Software: PyCharm
class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()
print(F.__mro__) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性

#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C
#python3中统一都是新式类
#pyhon2中才分新式类与经典类
'''
为了实现继承,python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止。
而这个MRO列表的构造是通过一个C3线性化算法来实现的。我们不去深究这个算法的数学原理,它实际上就是合并所有父类的MRO列表并遵循如下三条准则:
1.子类会先于父类被检查
2.多个父类会根据它们在列表中的顺序被检查
3.如果对下一个类存在两个合法的选择,选择第一个父类
继承的作用:
减少代码的重用
提高代码可读性
规范编程模式
'''


#一切皆文件
import abc #利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')

wenbenwenjian=Txt()

yingpanwenjian=Sata()

jinchengwenjian=Process()

#这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)

'''
抽象类的本质还是类，指的是一组类的相似性，包括数据属性（如all_type）和函数属性（如read、write），而接口只强调函数属性的相似性。
抽象类是一个介于类和接口直接的一个概念，同时具备类和接口的部分特性，可以用来实现归一化设计 
在python中，并没有接口类这种东西，即便不通过专门的模块定义接口，我们也应该有一些基本的概念。'''
''''
1多继承问题
在继承抽象类的过程中，我们应该尽量避免多继承；
而在继承接口的时候，我们反而鼓励你来多继承接口
接口隔离原则：
使用多个专门的接口，而不使用单一的总接口。即客户端不应该依赖那些不需要的接口。
2.方法的实现
在抽象类中，我们可以对一些抽象方法做出基础实现；
而在接口类中，任何方法都只是一种规范，具体的功能需要子类实现
'''


class Teacher:
    def __init__(self,name,age):
        self.set_info(name,age)

    def tell_info(self):
        print('姓名:{} 年龄:{}'.format(self.__name,self.__age))
    def set_info(self,name,age):
        if not isinstance(name,str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age,int):
            raise  TypeError('年龄必须是整型')
        self.__name = name
        self.__age = age
t = Teacher('tom',20)
t.tell_info()
t.set_info('dong',19)
t.tell_info()
#@property
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
class People:
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
p1 = People()
p1.name = 'dong'#OK，实际转化为s.set_score(60)
print(p1.name)#OK，实际转化为s.get_score()

#__slots__
class Students(object):
    __slots__ = ('name','age')


s = Students()
s.name = 'tom'
s.age = 25
#s.score = 99#错误.score没放到__slots__中去,所以不能绑定score属性
#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：


#类方法与静态方法
class Foo(object):
    '''类三种方法语法形式'''

    # 在类中定义普通方法，在定义普通方法的时候，必须添加self
    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

# 在类中定义静态方法，在定义静态方法的时候，不需要传递任何类的东西
    @staticmethod
    def static_method():
        print("是静态方法")

# 在类中定义类方法，在定义类方法的时候，需要传递参数cls  cls即为类本身
    @classmethod
    def class_method(cls):
        print("是类方法")

'''
在定义静态方法的时候，和模块中的方法没有什么不同，最大的不同就是在于静态方法在类的命名空间之间，而且在声明静态方法的时候，使用的标记为@staticmethod，表示为静态方法，在叼你用静态方法的时候，可以使用类名或者是实例名来进行调用，一般使用类名来调用
静态方法主要是用来放一些方法的，方法的逻辑属于类，但是有何类本身没有什么交互，从而形成了静态方法，主要是让静态方法放在此类的名称空间之内，从而能够更加有组织性。
在定义类方法的时候，传递的参数为cls.表示为类，此写法也可以变，但是一般写为cls。类的方法调用可以使用类，也可以使用实例，一般情况使用的是类。
6：在重载调用父类方法的时候，最好是使用super来进行调用父类的方法。静态方法主要用来存放逻辑性的代码，基本在静态方法中，不会涉及到类的方法和类的参数。类方法是在传递参数的时候，传递的是类的参数，参数是必须在cls中进行隐身穿'''
foo = Foo()
foo.instance_method()
foo.class_method()
foo.static_method()
print("---------------")
Foo.static_method()
Foo.class_method()
