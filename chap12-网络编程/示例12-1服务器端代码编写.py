from socket import socket, AF_INET, SOCK_STREAM

# AF_INET 用于Internet之间的进程通信
# SOCK_STREAM 表示的是用TCP协议编程

# (1) 创建socket
server_socket = socket(AF_INET, SOCK_STREAM)

# (2) 绑定地址
ip = '127.0.0.1'  # 等同于localhost
port = 8888
server_socket.bind((ip, port))

# (3) 监听
server_socket.listen(5)
print('服务器启动成功')

# (4) 接受连接
client_socket, client_address = server_socket.accept()  # 系列解包赋值
# (5) 接收数据
data = client_socket.recv(1024)
# 要求客户端发送过来的数据是使用utf-8编码
print('客户端发送过来的数据为:', data.decode('utf-8'))
# (6) 发送数据 是以字节（bytes）形式表示的数据，b 表示这是一个字节字符串，网络传输必须使用字节格式。
client_socket.send('hello client, your address is {}'.format(client_address).encode('utf-8'))
# (7) 关闭套接字
server_socket.close()
