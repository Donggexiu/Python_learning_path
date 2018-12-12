#!/usr/bin/env/python
# _*_coding:utf-8_*_
# @Time : 2018/12/10 13:55
# @Author : Dxd
# @Site : 
# @File : 网络编程练习题.py
# @Software: PyCharm
#写一个程序，要求用户输入用户名和密码，要求密码长度不少于6个字符，且必须以字母开头，如果密码合法，则将该密码使用md5算法加密后的十六进制概要值存入名为password.txt的文件，超过三次不合法则退出程序；
import hashlib
import re
import json
def func():
    count = 0
    while count <3:
        username = input('请输入账号:').strip()
        password = input('请输入密码:').strip()
        if re.search('^([A-Z]|[a-z])',password) and len(password) >=6:
            md5_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            file_obj = {'username':username,
                        'password':md5_password}
            with open('password.txt','w+',encoding='utf-8') as f:
                json.dump(file_obj,f)

            break

        else:
            print('请输入合法的密码')
            count += 1
    else:
        print('say good_bye')

if __name__ == '__main__':
    func()

#12、写一个程序，使用socketserver模块，实现一个支持同时处理多个客户端请求的服务器，要求每次启动一个新线程处理客户端请求；
import socketserver
#服务端
class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                if not data:break
                print('收到的数据:',data.decode())
                self.request.send(data.upper())

            except Exception as e:
                print(e)
                break


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8888),Handler)
    server.serve_forever()

import socket
ip_port = ('127.0.0.1',8888)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ip_port)
while True:
    msg = input(">>>>").strip()
    if not msg:
        continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data)