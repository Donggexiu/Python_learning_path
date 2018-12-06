#!/usr/bin/env/python_SQLAlchemy
# _*_coding:utf-8_*_
# @Time : 2018/11/21 10:19
# @Author : 小仙女
# @Site : 
# @File : 购物车.py
# @Software: PyCharm
goods_list = [('coffee',30),('bike',599), ('book',49), ('earphone',88),
    ('pen',99),
    ('computer',3499),]

shopping_list = []
salary = input('请输入你的工资:')
if salary.isdigit():
    salary = int(salary)
    while 1:
        for index,item in enumerate(goods_list):
            print(index,item)

        user_choice = input('请选择您购买的商品:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice<len(goods_list) and user_choice>=0:
                p_item = goods_list[user_choice]
                if p_item[1] <=salary:
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print('工资剩余%s,商品买了%s'%(salary,p_item))
                else:
                    print('钱不够')
            else:
                print('商品不存在')

        elif user_choice == 'q':
            print('---shopping----list')
            for p in shopping_list:
                print(p,end=' ')
            print('')
            print('您的余额:',salary)
            exit()
        else:
            print('没钱了')

#升级版本
# 1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
# 2、允许用户根据商品编号购买商品
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4、可随时退出，退出时，打印已购买商品和余额
# 5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
#     扩展需求：
#         1、用户下一次登录后，输入用户名密码，直接回到上次的状态，
#         即上次消费的余额什么的还是那些，再次登录可继续购买
#         2、允许查询之前的消费记录
exit_flag = False
user_file = open('userinfo.txt','r+')
user_info = user_file.read()
user_info = eval(user_info)


