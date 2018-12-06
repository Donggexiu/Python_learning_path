#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/12 14:37
# @Author : 小仙女
# @Site : 
# @File : 列表推导式.py
# @Software: PyCharm
# list_a = [name.upper() for name in names if len(name) >3]
list_b = [(x,y) for x in range(5) if x%2==0 for y in range(5) if y %2==1]
print(list_b)
M = [[1,2,3],[4,5,6],[7,8,9]]
list_c = [row[2] for row in M]
print(list_c)
list_new = list()