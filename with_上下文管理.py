#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/19 15:53
# @Author : 小仙女
# @Site : 
# @File : with_上下文管理.py
# @Software: PyCharm
#上述叫做上下文管理协议，即with语句，为了让一个对象兼容with语句，必须在这个对象的类中声明__enter__和__exit__方法
#上下文管理协议
class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
        # return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')


with Open('a.txt') as f:
    print('=====>执行代码块')
    # print(f,f.name)
# __exit__()中的三个参数分别代表异常类型，异常值和追溯信息,with语句中代码块出现异常，则with后的代码都无法执行
class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
        print(exc_type)
        print(exc_val)
        print(exc_tb)


with Open('a.txt') as f:
    print('=====>执行代码块')
    raise AttributeError('***着火啦,救火啊***')
print('0' * 100)  # ------------------------------->不会执行
# 如果__exit()返回值为True,那么异常会被清空，就好像啥都没发生一样，with后的语句正常执行
class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True


with Open('a.txt') as f:
    print('=====>执行代码块')
    raise AttributeError('***着火啦,救火啊***')
print('0' * 100)  # ------------------------------->会执行
# 练习：模拟Open
class Open:
    def __init__(self, filepath, mode='r', encoding='utf-8'):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        # print('enter')
        self.f = open(self.filepath, mode=self.mode, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('exit')
        self.f.close()
        return True

    def __getattr__(self, item):
        return getattr(self.f, item)


with Open('a.txt', 'w') as f:
    print(f)
    f.write('aaaaaa')
    f.wasdf  # 抛出异常，交给__exit__处理
# 用途或者说好处：
# 使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
# 在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处