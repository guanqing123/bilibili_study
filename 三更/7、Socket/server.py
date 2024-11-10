# server 服务端 后台
from socket import *

# 1、准备一台电话机 / 创建一个套接字
server_socket = socket()
# 2、电话机绑定号码 / 套接字绑定网络地址
server_socket.bind((gethostname(), 8888))
# 网络地址的格式：(ip, port)
# ip地址
# port端口 1-65535之间 都取这个: 1025-65535
# 3、电话机开启监听 / 套接字开启监听
server_socket.listen()
# 4、接电话 / 接受连接,转交给另一个套接字
while True:
    s, addr = server_socket.accept()
    # 175.0.118.228
    print(addr)  # 打印一下对方的网络地址

    # 连上之后 后台
    s.send('你好'.encode())  # 发送
    print('1.关机\n2.重启\n')
    choise = input('请选择:')
    s.send(choise.encode())
