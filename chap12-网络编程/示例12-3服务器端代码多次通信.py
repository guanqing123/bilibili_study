from socket import socket

# 创建socket对象
server_socket = socket()

server_socket.bind(('localhost', 9999))
server_socket.listen(5)
print('服务器启动成功')

while True:
    # 这里有bug, 再次进入循环的时候, 下面代码是一个新获取的连接, 会被阻塞, 下面接收的代码不会被执行到
    # 如果这个时候, 有新的连接进来, client_socket 又被新的连接赋值, 上一个连接再也接收不到信息了
    client_socket, client_address = server_socket.accept()

    # 接收客户端传来端数据
    data = client_socket.recv(1024).decode('utf-8')
    if data == 'bye':
        break
    elif data != '':
        print('接收到客户端的信息为：', data)

    say = input('请输入要发送给客户端的信息：')
    client_socket.send(say.encode('utf-8'))
    if say == 'bye':
        break

client_socket.close()
server_socket.close()
