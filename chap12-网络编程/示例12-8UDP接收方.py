from socket import socket, AF_INET, SOCK_DGRAM

# (1)创建socket对象
recv_socket = socket(AF_INET, SOCK_DGRAM)
# (2)绑定IP和端口
recv_socket.bind(('127.0.0.1', 9999))
# (3)接收来自发送方的数据
recv_data, addr = recv_socket.recvfrom(1024)
print('接收到的数据为:', recv_data.decode('utf-8'))

# (4)准备回复对方的数据
reply_data = input('请输入要回复的数据:')
recv_socket.sendto(reply_data.encode('utf-8'), addr)

# (5)关闭
recv_socket.close()