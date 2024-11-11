# server 服务端 后台
import sys
from socket import *

import cv2

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
    # s.send('你好'.encode())  # 发送
    # print('1.关机\n2.重启\n')
    # choise = input('请选择:')
    # s.send(choise.encode())

    # 文件传输
    # 接受对方的文件的大小的数据
    # filesize = int(s.recv(1024).decode())
    # s.send('ok'.encode())

    # 接收文件的数据 回复
    # cursize = 0  # 当前的大小!
    # with open('321.png', 'wb') as file:
    #     while cursize < filesize:  # 只要刻度小于目标 一直循环
    #         data = s.recv(2048)
    #         file.write(data)
    #         cursize += len(data)
    #         # print(len(data))
    #     s.send('ok'.encode())

    # 摄像头
    cap_is_open = s.recv(1024).decode()
    if cap_is_open == 'error':
        sys.exit(1)
    else:
        s.send('ok'.encode())
        # 1、接受摄像头的一帧图像
        filesize = int(s.recv(1024).decode())
        cursize = 0  # 当前的大小!
        with open('2.jpg', 'wb') as file:
            while cursize < filesize:  # 只要刻度小于目标 一直循环
                data = s.recv(2048)
                file.write(data)
                cursize += len(data)
                # print(len(data))
            s.send('ok'.encode())

        # 2、显示出来
        # 2.1、创建一个窗口叫cpature
        cv2.namedWindow('capture')
        # 2.2、加载一张图片image
        image = cv2.imread('2.jpg')
        # 2.3、把image显示在capture
        cv2.imshow('capture', image)
        # 2.4、设置刷新时间
        cv2.waitKey(20)
