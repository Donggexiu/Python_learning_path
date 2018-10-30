from socket import  *
def main():
    #创建socket
    tcp_client = socket(AF_INET,SOCK_STREAM)
    #目的信息
    server_ip = input('请输入服务器ip:')
    server_port = int(input('请输入服务器port:'))
    tcp_client.connect((server_ip,server_port))
    #输入需要下载的文件名
    file_name = input('请输入要下载的文件名:')
    tcp_client.send(file_name.encode('utf-8'))
    #接收对方发送过来的数据,最大接收1024个字节
    recv_data = tcp_client.recv(1024)
    if recv_data:
        with open('[接收]' + file_name,'wb') as f:
            f.write(recv_data)



    tcp_client.close()

if __name__ == '__main__':
    main()
