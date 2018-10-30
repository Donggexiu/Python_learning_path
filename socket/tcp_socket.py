from socket import *
#创建socket
tcp_client = socket(AF_INET,SOCK_STREAM)
#目的信息
server_ip = input('请输入服务器ip:')
server_port = int(input('请输入服务器端口:'))
#连接服务器
tcp_client.connect((server_ip,server_port))
#提示用户输入数据
send_data = input('请输入你要发送的数据:')
tcp_client.send(send_data.encode('utf-8'))
#接收对方发送过来的数据,最大接收1024个字节
recv_data = tcp_client.recv(1024)
print('接收的数据为:',recv_data.decode('gbk'))
#关闭套接字
tcp_client.close()


# 创建socket
tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 本地信息
address = ('', 7788)

# 绑定
tcp_server_socket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
tcp_server_socket.listen(128)

# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
client_socket, clientAddr = tcp_server_socket.accept()

# 接收对方发送过来的数据
recv_data = client_socket.recv(1024)  # 接收1024个字节
print('接收到的数据为:', recv_data.decode('gbk'))

# 发送一些数据到客户端
client_socket.send("thank you !".encode('gbk'))

# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
client_socket.close()