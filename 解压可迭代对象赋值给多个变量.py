''''
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么
怎样才能从这个可迭代对象中解压出 N 个元素出来？
'''
#Python 的星号表达式可以用来解决这个问题
import math
# def drop_first_last(grades):
#     first,*midle,last = grades
#     return avg(midle)
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)
records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
#星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
# 代码示例：
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*friends,homedir,sh = line.split(':')
print(uname)
print(homedir)
print(sh)
