# import socket
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.close()

# '''
# 1.udp创建客户端套接字2.发送接收数据3.关闭套接字
# '''
# from socket import *
# #创建udp套接字
# # udp_socket = socket(AF_INET,SOCK_DGRAM)
# #准备接收方的地址
# #'192.168.101.204'表示目的ip地址 8080表示目的端口号
# # dest_addr = ('192.168.101.204',8080)
# # # 从键盘获取数据
# # send_data = input('请输入需要发送的数据:')
# # #发送数据到自定的电脑上的制定程序中
# # udp_socket.sendto(send_data.encode('utf-8'),dest_addr)
# # udp_socket.close()
#
# #2.udp网络程序-发送.接收数据
# udp_socket = socket(AF_INET,SOCK_DGRAM)
# #准备接收方的地址
# dest_addr = dest_addr = ('192.168.101.204',8080)
# #从键盘获取数据
# send_data = input('请输入需要发送的数据:')
# #发送数据到自定的电脑上的制定程序中
# udp_socket.sendto(send_data.encode('utf-8'),dest_addr)
# #5接收对方发送的数据
# recv_data = udp_socket.recvfrom(1024)#表示本次接收最大字节数
# #显示对方发送的数据 recv_data是一个元祖
# #第一个数据是对方的数据,第二个数据是端口
# print(recv_data[0].decode('gbk'))
# print(recv_data[1])
# udp_socket.close()
import socket

def send_msg(udp_socket):
    '''获取键盘数据,并将其发给对方'''
    msg = input('\n请输入要发送的数据:')
    #2输入对方的ip地址,端口
    dest_ip = input('请输入对方的ip地址:')
    dest_port = int(input('请输入对方的端口:'))
    #发送数据
    udp_socket.sendto(msg.encode('utf-8'),(dest_ip, dest_port))
def recv_msg(udp_socket):
    '''接收数据显示'''
    #1接收数据
    recv_msg = udp_socket.recvfrom(1024)
    #解码
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode('utf-8')
    #显示接收到的数据
    print('>>>%s:%s'%(str(recv_ip),recv_msg))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('',7890)
    udp_socket.bind(local_addr)
    while 1:
        print('='*30)
        print("1:发送消息")
        print("2:接收消息")
        print("=" * 30)
        op_num = input("请输入要操作的功能序号:")
        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            break

if __name__ == '__main__':
    main()