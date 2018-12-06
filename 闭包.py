#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/9 9:21
# @Author : 小仙女
# @Site : 
# @File : 闭包.py
# @Software: PyCharm
# 闭包函数的实例子
'''
1）变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；
（2）只有模块、类、及函数才能引入新作用域；
（3）对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；
（4）内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用
nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。
'''
# outer是外部函数a和b都是外函数的临时变量

def outer(a):
    b = 10

    # inner 是内函数
    def inner():
        # 在内部函数中,用到了外部函数的临时变量
        print(a + b)

    # 外部函数的返回值是内函数的引用
    return inner


if __name__ == '__main__':
    # 在这里我们调用外部函数传入参数5
    # 此时外函数两个临时变量a是5,b是10,并创建了内函数,然后把函数的引用返回给了demo,
    # 外函数结束的时候内部函数将会用到自己的临时变量,这两个临时变量就不会释放,会绑定给这个内部函数
    demo = outer(5)
    # 我们调用内部函数,看一看内部函数是不是使用外部函数的临时变量
    # demo存了外函数的返回值,也就是inner函数的引用,这里相当于执行了inner函数
    demo()
    demo2 = outer(7)
    demo2()

'''
闭包中内函数修改外函数局部变量：
在闭包内函数中，我们可以随意使用外函数绑定来的临时变量，但是如果我们想修改外函数临时变量数值的时候发现出问题了！咋回事捏？？！
在基本的python语法当中，一个函数可以随意读取全局数据，但是要修改全局数据的时候有两种方法:1 global 声明全局变量 2 全局变量是可变类型数据的时候可以修改
在闭包内函数也是类似的情况。在内函数中想修改闭包变量（外函数绑定给内函数的局部变量）的时候：
　 在python3中，可以用nonlocal 关键字声明 一个变量， 表示这个变量不是局部变量空间的变量，需要向上一层变量空间找这个变量。'''


# 修改闭包变量的实例
# outer是外部函数a和b都是外函数的临时变量
def outer(a):
    b = 10  # a和b 都是闭包变量

    def inner():
        # 内函数中想修改闭包变量
        nonlocal a, b
        b += 1
        a += 1
        print(a)
        print(b)

    return inner


if __name__ == '__main__':
    demo = outer(5)
    demo()


def outer(x):
    def inner(y):
        nonlocal x
        x += y
        return x

    return inner


'''
用闭包的过程中，一旦外函数被调用一次返回了内函数的引用，虽然每次调用内函数，是开启一个函数执行过后消亡，但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量
'''
if __name__ == '__main__':
    a = outer(10)
    print(a(3))
    print(a(1))
    '''下面让我们来了解一下闭包的包到底长什么样子。其实闭包函数相对与普通函数会多出一个__closure__的属性，里面定义了一个元组用于存放所有的cell对象，每个cell对象一一保存了这个闭包中所有的外部变量。'''
#写函数，计算传入的字符串中数字，字母，空格，以及其他的个数
def func(s):
    num = 0
    space_num = 0
    digit_num = 0
    others = 0
    for i in s:
        if i.isdigit():
            digit_num +=1
        elif i.isspace():
            space_num +=1
        elif i.isalh:
            pass


