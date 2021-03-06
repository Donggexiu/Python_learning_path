#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/12 10:29
# @Author : 小仙女
# @Site : 
# @File : 生成器.py
# @Software: PyCharm
#生成器:生成器是一类特殊的迭代器.
'''
当我们需要编写一个迭代器的时候，发现迭代器很麻烦，我们需要写__next__和__iter__两个方法：
_iter__方法负责返回一个迭代器（在迭代器中返回自己，在可迭代对象中返回帮助自己迭代的迭代器）
__next__方法做两件事：
1 如果当前要获取的元素没有超出界限，就返回当前元素，然后自己指向为下一个元素等待返回；
2 如果上次反回了最后一个元素，这一次再调用next的时候已经没有元素了，就抛出StopIteration异常。
'''
#生成器的实现:
# 1()括号内放入列表推导表达式,返回一个生成器对象
#yield 关键字函数.
#1列表推导式
#生成前十个偶数的列表
list = [x*2 for x in range(11)]
print(list)
#生成前十个偶数的生成器
iterator = (x*2 for x in range(11))
print(type(iterator))
for num in iterator:
    print(num)
'''
从代码种我们可以看出，普通的列表推导式，放到括号当中，接收的对象是一个生成器对象。
    它也是一个迭代器对象，可以放到for循环当中操作，
    也可以用next方法一个一个取出元素，还能看到当越界的时候抛出了StopIteration的异常
    这些复杂的东西都被python帮我们封装了，不需要我们自己操心去处理了。
'''
#yield关键字函数
def odd(n):
    for i in range(0,n+1,2):
        yield i
'''从代码种我们可以看出，把我们平时想要得到的数据 用yield关键字声明一下，就可以得到生成器了。
python看到yield会把这个函数帮助我们继续封装，加上next方法和iter方法，并且看到越界后会帮助我们抛出异常。
这些复杂的与业务逻辑无关的已经无需我们编程者来操心了，python帮助我们完成了。'''
gen10 = odd(10)
for i in gen10:
    print(i)

'''
现在说一下yield i 这句话到底发生了什么：
    首先获得了一个迭代器对象gen = odd(20)
    当函数执行到yield i 的时候 实际上函数会把i的数值抛出来，我们调用next(gen)的时候获取了yield 后面的值，然后函数就会暂停，等待下一次再调用next(gen)的时候，函数从yield继续向下执行，直到遇到yield的时候又返回了i的值，然后函数再暂停，等待下一次唤醒。这个循环一直做，到函数结束的时候，python帮助咱们抛出了异常。
yield关键字函数的扩展：
    返回值：果我们的生成器yield关键字函数当中，结束时候自己设置了返回值，这个返回值会被抛出的异常接收，存到了异常对象的value属性里面。
    两种唤醒方式：
        1 next(gen) 之前讨论过，调用next后，函数从上一次抛出一个数据暂停之后继续执行，直到遇到yield时候抛出来i返回给next函数再暂停，等待下一次唤醒。
        2 gen.send( mess ) 这个方法也能够唤醒生成器函数，并且得到新的yield抛出数据，不同点是：
            如果我们 把上面的yield抛出改成  msg = yield i , 那么我们用send传入的mess将会在唤醒的时候被msg接收到。如果我们用next方法唤醒，则msg接收到None。
'''
#yield关键字函数
#yield关键字函数的生成器
#一个n以内偶数的生成器
def odd(n):
    for i in range(0,n+1,2):
        '''代码执行从右向左,当遇到yield的时候,会把i抛出给next的调用返回,然后函数停在这里
            下一次外面调用next或者send方法唤醒的时候,msg=开始执行,上一次停在了yield这里,左边还没执行,然后在
            然后再碰到yield i的时候把i抛出来再暂停
            '''
        msg = yield i
        '''
        当函数执行结束的时候python认为迭代器结束了,帮助外面抛出异常,返回值会被异常对象接收存在了value属性里面'''
    return '哈哈'
#用gen获取一个生成器的对象
gen = odd(5)
#生成器也是迭代器,用next方法唤醒yield暂停,继续向下执行
print(next(gen))#0
print(next(gen))#2
print(gen.send('传入数据'))#传入数据4,这个时候在函数里面会打印出来传入的传入数据,并返回了下一次的i也就是4 然后暂停
#这时候不论next还是send,迭代器已经结束了python会帮我们抛出异常,函数的返回值会被异常对象接收存在value属性里
try:
    print(next(gen))
except StopIteration as e:
    print(e.value)
'''生成器有两种实现方式：
1 () 括号内 放入 列表生成式
2 yield 关键字函数：正常写一个业务逻辑函数，把想迭代的数据用yield关键字声明。函数执行到yield关键字会把后面的数值抛出去，然后暂停，等待下一次唤醒。
两种唤醒方式： gen = 生成器函数()   我们拿到一个生成器对象gen
1 next(gen)  能够唤醒上一次暂停，函数会从上一次抛出数之后继续执行到再次遇见yield i 把i抛回来 后再暂停
2 gen.send(mess) 唤醒上一次暂停，并且把mess传入给接收yield 的变量，让我年后函数继续执行遇到 msg = yield i  的时候把i抛出来返回，再暂停。
生成器实质： 它是python提供给我们快速写一个迭代器的功能。我们只关心业务逻辑，把功能实现了，至于迭代器内部的iter方法和next方法已经不用我们操心了，迭代过后的抛出异常也为我们封装好好了。　
因为它会被封装成迭代器，所以我们可以把生成器对象放入for in 循环中，也可以用next() 方法去获取元素！！'''