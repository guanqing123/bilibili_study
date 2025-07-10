import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 9999))
print('已连接服务器！')

while True:
    # 向服务器发送数据
    send = input('请输入您想对服务器说的话：')
    client_socket.send(send.encode('utf-8'))
    if send == 'bye':
        break

    # 接收服务器发送过来的数据
    recv = client_socket.recv(1024).decode('utf-8')
    if recv == 'bye':
        break
    elif recv != 'bye':
        print('服务器说：', recv)

client_socket.close()