from socket import socket, AF_INET, SOCK_DGRAM

# (1)创建 socket
send_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    # (2)准备发送的数据
    data = input('客户说:')
    ip_port = ('127.0.0.1', 8888)
    # (3)发送数据
    send_socket.sendto(data.encode('utf-8'), ip_port)
    if data == 'bye':
        break
    # (4)接收来自客服人员的回复数据
    recv_data, addr = send_socket.recvfrom(1024)
    print(f'客服回：{recv_data.decode("utf-8")}')
    if recv_data.decode('utf-8') == 'bye':
        break
# (5)关闭 socket
send_socket.close()
