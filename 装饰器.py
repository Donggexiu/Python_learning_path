#!/usr/bin/env/python
# _*_coding:utf-8_*_
# @Time : 2018/11/9 10:04
# @Author : 小仙女
# @Site : 
# @File : 装饰器.py
# @Software: PyCharm
# 装饰器函数,传入目标函数做参数
import time
def decorator(func):
    # 实际调用目标函数会发生调用inner
    # 所以我门让inner接收不定长参数,我们再把不定参数传给目标函数func
    # 这样不论我们传入什么参数目标函数都能接收到!
    def inner(*args, **kwargs):
        print('装饰器函数中..目标函数执行之前的操作!!')
        # 我们设置一个变量接收目标函数返回值,在inner结束的时候再把返回值返回去
        # python不同于其他语言,即使我们没有编写func的返回值,也会返回None,所以这里不会报错
        res = func(*args, **kwargs)
        print('装饰器函数中..目标函数执行之后的操作!!')
        return res

    return inner


# 这样编写的装饰器,在外部看来,我们就可以传入参数给目标函数,同时也可以正常接收目标函数返回的参数!

@decorator  # 实际上会把destination = decorator(destination)
# 把目标函数传入的装饰器返回了inner给destination
# 此后我们在调用destination实际上调用了inner函数的一个对象
def destination(a):
    print('目标函数接收到参数:%s' % a)
    return '目标函数的返回值:%s' % a


if __name__ == '__main__':
    # 这里实际调用了inner函数的对象,我们传入参数和接收返回值都没有问题了
    res = destination(10)
    print(res)
    '''
        执行结果:
             装饰器函数中。。目标函数执行之前的操作！！
             目标函数接受到参数:10
             装饰器函数中。。目标函数执行之后的操作！！
             目标函数的返回值10
    '''


# 多层装饰器的嵌套
def decorator_out(func):
    def inner(*args, **kwargs):
        print('外装饰器前置操作')
        res = func(*args, **kwargs)
        print('外装饰器后置操作')
        return res

    return inner


def decorator_in(func):
    def inner(*args, **kwargs):
        print('内装饰器前置操作')
        res = func(*args, **kwargs)
        print('内装饰后置操作')
        return res

    return inner


# 目标函数被两个装饰器装饰
'''
这里实际上会发生的情况是login = decoratoe_out(decorator_in(destination))
先in装饰器装饰目标函数之后,把inner返回给destination,然后out装饰器在对新的destination
进行装饰,out里的func存了in装饰器装饰过的destination函数,又把inner返回给destination
这时候在执行目标函数destination()实际上
1执行out装饰器的inner() 执行到func的时候 执行in装饰器的inner
2 在内装饰器inner中执行func才是原来的目标函数
3 目标函数执行完跳出到in装饰器的inner
4 in装饰器函数inner执行完 相当于out装饰器的func执行完 跳到out装饰器的inner中
5 out装饰器执行结束，全部过程结束
'''


@decorator_out
@decorator_in
def destination():
    print('目标函数')


if __name__ == '__main__':
    destination()


# 当多层装饰器嵌套的时候，实际上先内层装饰器装饰目标函数外层装饰器会对内层装饰器装饰的结果进行再装饰
# 可选择装饰器
# 我们传入一个flag决定是不是要执行目标函数之后的操作
def flagOperation(flag):
    def decorator(func):
        def inner(*args, **kwargs):
            print('装饰器前置操作')
            res = func(*args, **kwargs)
            if flag:  # 如果为真
                print('我是后置操作')
            return res

        return inner

    return decorator


'''
@flagOperation(True)这里实际上先执行了flagOperation(True),返回了decorator装饰器,并且把flag的值是True绑定给了他,这时候
用带着flag的decorator对目标函数进行装饰,相当于@decorator带着一个flag
'''


@flagOperation(True)
def destination():
    print('目标函数')


@flagOperation(False)
def destination2():
    print('目标函数2')


if __name__ == '__main__':
    destination()
    destination2()


# 类装饰器
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('类装饰器前置操作')
        self.func()
        print('类装饰器后置操作')


@Decorator
def login():
    print('login now')


if __name__ == '__main__':
    login()



def show_time(func):
    def wrapper(a, b):
        start_time = time.time()
        ret = func(a, b)
        end_time = time.time()
        print('spend %s' % (end_time - start_time))
        return ret

    return wrapper


@show_time  # add=show_time(add)
def add(a, b):
    time.sleep(1)
    return a + b


print(add(2, 5))

'-练习题-'
#1.编写三个函数,每个函数执行的时间不一样的
def verify(flag):
    def decorator(func):
        def wrapper():
            start_time = time.time()
            if flag:
                func()
            end_time = time.time()
            print('spend_time %s'%(end_time-start_time))
        return wrapper
    return decorator
@decorator
def foo1():
    print('hello foo1')
    time.sleep(1)
print(foo1())
@decorator
def foo2():

    print('hello foo2')
    time.sleep(2)
print(foo2())
@decorator
def foo3():
    print('hello foo3')
    time.sleep(3)
print(foo3())