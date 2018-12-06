#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/9 14:05
# @Author : 小仙女
# @Site : 
# @File : 高阶函数.py
# @Software: PyCharm
'''
定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
'''
'''
. 必须有一个明确的结束条件
2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3. 递归效率不高，递归层次过多会导致栈溢出(在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返     回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。)
'''
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i

    return result
print(factorial(4))
#递归
def factorial_new(n):
    if n == 1:
        return 1
    return n*factorial_new(n-1)
print(factorial_new(4))

#斐波那契额数列
def fibo(n):
    if n <=1:
        return n
    return fibo(n-1) +fibo(n-2)

#内置函数filter(function,sequence)
#对sequence中的item依次执行function(item)，将执行结果为True的item做成一个filter object的迭代器返回。可以看作是过滤函数。
str = ['a','b','c','d']
def fun1(s):
    if s !='a':
        return s
res = filter(fun1,str)
print(list(res))
'--2--map(function,sequences)'
str = ['1','2','3','4']
def func2(s):
    return s +'alvin'

res2 = map(func2,str)
print(list(res2))


