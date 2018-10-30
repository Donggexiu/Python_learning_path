from socket import *
import sys

def get_filecontent(file_name):
    '''获取文件内容'''
    try:
        with open(file_name,'rb') as f:
            content = f.read()
        return content
    except:
        print('没有下载的文件:%s'%(file_name))
def main():
    #创建socket
    tcp_server = socket(AF_INET,SOCK_STREAM)
    #本地消息
    address = ('', 8200)
    #绑定本地消息
    tcp_server.bind(address)
    #将主动套接字变为被动套接字
    tcp_server.listen(128)
    while 1:
        client_socket ,clientAddr = tcp_server.accept()
        #接收对方发送过来的数据
        recv_data = client_socket.recv(1024)
        file_name = recv_data.decode('utf-8')
        print('请求下载的文件名:%s'%file_name)
        file_content = get_filecontent(file_name)
        #发送文件的数据给客户端
        #因为获取打开文件是以rb方式打开,所以file_content中的数据已经是二进制的数据,因此不需要encode编码
        if file_content:
            client_socket.send(file_content)

        #关闭套接字
        client_socket.close()
    tcp_server.close()
if __name__ == '__main__':
    main()





