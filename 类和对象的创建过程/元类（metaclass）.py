#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/19 16:10
# @Author : 小仙女
# @Site : 
# @File : 元类（metaclass）.py
# @Software: PyCharm
'''
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义元类（不自定义时，默认用type），然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是元类创建出来的“实例”。
'''
# 默认情况下，类是使用type()
# 构造的。类主体在一个新的名称空间中执行，类名在本地绑定到类型的结果(名称、基、名称空间)。
# 可以通过在类定义行中传递元类关键字参数来定制类创建过程，或者从包含此类参数的现有类继承。在下面的示例中，MyClass和MySubclass都是Meta的实例:
class Meta(type):
    pass
class MyClass(metaclass=Meta):
    pass
class MySubClass(MyClass):
    pass

#使用metaclass的两种方式
class MyType(type):# 自定义一个type的派生类
    def __init__(self,*args,**kwargs):
        print('xx')
        super(MyType,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls,*args, **kwargs)
        cls.__init__(obj,*args, **kwargs)
        return obj

def with_metaclass(base):
    return MyType("MyType2",(base,),{})

# 方式一
class Foo(metaclass=MyType):# metaclass=MyType,即指定了由MyType创建Foo类，当程序运行，用到class Foo时，即调用MyType的__init__方法，创建Foo类
    def __init__(self,name):
        self.name = name


#方式二    在Flask的wtform的源码中用到过
# class Foo(with_metaclass(object)):
#     def __init__(self,name):
#         self.name = name

a=Foo('name')
#  方式一:即用类的形式
# 执行代码后，当遇到class Foo时即声明要创建一个Foo类，就会调用type的__init__方法创建类，由于此处（metaclass=MyType），即指定了Foo类的创建方式，所以会执行type的派生类MyType的__init__方法，创建Foo类，打印一次'xx'
#  *一般情况下, 如果你要用类来实现metaclass的话，该类需要继承于type，而且通常会重写type的__new__方法来控制创建过程。
# * 在metaclass里面定义的方法会成为类的方法，可以直接通过类名来调用
# 方式二：用函数的形式
# 构建一个函数，返回一个type的派生类对象，例如叫type的派生类, 需要3个参数：name, bases, attrs
# name: 类的名字
# bases: 基类，通常是tuple类型
# attrs: dict类型，就是类的属性或者函数
'''metaclass 原理'''
#metaclass的原理其实是这样的：当定义好类之后，创建类的时候其实是调用了type的__new__方法为这个类分配内存空间，创建好了之后再调用type的__init__方法初始化（做一些赋值等）。所以metaclass的所有magic其实就在于这个__new__方法里面了。
# 说说这个方法：__new__(cls, name, bases, attrs)
# cls: 将要创建的类，类似与self，但是self指向的是instance，而这里cls指向的是class
# name: 类的名字，也就是我们通常用类名.__name__获取的。
# bases: 基类
# attrs: 属性的dict。dict的内容可以是变量(类属性），也可以是函数（类方法）。
# 所以在创建类的过程，我们可以在这个函数里面修改name，bases，attrs的值来自由的达到我们的功能。这里常用的配合方法是
# getattr和setattr（just an advice)
'''
4、实例化对象的完整过程
'''
class Foo(Bar):
    pass
'''
当我们写如这段代码时，Python做了如下的操作：
Foo中有metaclass这个属性吗？如果是，Python会在内存中通过metaclass创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。如果Python没有找到metaclass，它会继续在Bar（父类）中寻找metaclass属性，并尝试做和前面同样的操作。如果Python在任何父类中都找不到metaclass，它就会在模块层次中去寻找metaclass，并尝试做同样的操作。如果还是找不到metaclass,Python就会用内置的type来创建这个类对象。
把上面这段话反复读几次，现在的问题就是，你可以在metaclass中放置些什么代码呢？
答案就是：可以创建一个类的东西。
那么什么可以用来创建一个类呢？
type，或者任何使用到type或者子类化type的东东都可以。
以上面的代码为例，我们实例化一个对象obj=Foo()时，会先执行Foo类的__new__方法，没写时，用父类的__new__方法，创建一个对象，并返回，然后执行__init__方法（自己有就用自己的，没有就用父类的），对创建的对象进行初始化。
obj()会执行Foo类的__call__方法，没有则用父类的
我们现在已经知道，类也是对象，是元类的对象，即我们实例化一个类时，调用其元类的__call__方法。
元类处理过程：定义一个类时，使用声明或者默认的元类对该类进行创建，对元类求type运算，得到父元类（该类声明的元类的父元类），调用父元类的__call__函数，在父元类的__call__函数中, 调用该类声明的元类的__new__函数来创建对象（该函数需要返回一个对象（指类）实例），然后再调用该元类的__init__初始化该对象（此处对象是指类，因为是元类创建的对象），最终返回该类
1.对象是类创建，创建对象时候类的__init__方法自动执行，对象()执行类的 __call__ 方法
2.类是type创建，创建类时候type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
'''
'''
原始type的__call__应该是参数结构应该是：
　metaname, clsname, baseclasses, attrs

原始type的__new__
　metaname, clsname, baseclasses, attrs
原始type的__init__

　class_obj, clsname, baseclasses, attrs

元类的__new__和__init__影响的是创建类对象的行为，父元类的__call__控制对子元类的 __new__，__init__的调用，就是说控制类对象的创建和初始化。父元类的__new__和__init__由更上层的控制，

一般来说，原始type是最初的父元类，其__new__和__init__是具有普遍意义的，即应该是分配内存、初始化相关信息等

元类__call__影响的是创建类的实例对象的行为，此时如果类自定义了__new__和__init__就可以控制类的对象实例的创建和初始化
__new__和__init__ 影响的是创建对象的行为，当这些函数在元类中时，影响创建的是类；同理，当这俩个函数在普通类中时，影响创建的是普通的对象实例。

__call__ 影响()调用行为, __call__是在创建类的时候调用，即: class Test(object): __metaclass__=type, 定义类时就是创建类，此时会调用元类的__call__，如果元类有继承，子元类定义时执行的是父元类的__call__。

             如果是普通类实例化对象，调用的是普通类的__call__

'''