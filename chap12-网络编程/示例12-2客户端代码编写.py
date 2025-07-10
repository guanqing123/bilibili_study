import socket

# (1)创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# (2)连接服务器
client_socket.connect(('127.0.0.1', 8888))

# (3)发送数据
client_socket.send('hello, server'.encode('utf-8'))

# (4)接收数据
data = client_socket.recv(1024)
print(data.decode('utf-8'))

# (5)关闭套接字
client_socket.close()
