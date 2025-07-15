from socket import socket, AF_INET, SOCK_DGRAM

# (1)创建 socket
recv_socket = socket(AF_INET, SOCK_DGRAM)
# (2)绑定IP地址和端口
recv_socket.bind(('127.0.0.1', 8888))
while True:
    # (3)接收数据
    recv_data, addr = recv_socket.recvfrom(1024)
    print('客户说:', recv_data.decode('utf-8'))
    if recv_data.decode('utf-8') == 'bye':
        break
    # (4)准备回复数据
    reply_data = input('客服回:')
    recv_socket.sendto(reply_data.encode('utf-8'), addr)
    if reply_data == 'bye':
        break

# (5)关闭套接字
recv_socket.close()
