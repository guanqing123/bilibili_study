from socket import socket, AF_INET, SOCK_STREAM


def start_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    ip = '127.0.0.1'
    port = 8899
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print('服务器启动成功,等待客户端连接...')

    try:
        while True:  # 持续等待新客户端连接
            client_socket, client_address = server_socket.accept()
            print(f'客户端 {client_address} 已连接')

            try:
                while True:  # 持续与当前客户端对话
                    # 接收客户端消息
                    data = client_socket.recv(1024).decode('utf-8')
                    if not data or data.lower() == 'bye':
                        print(f'客户端 {client_address} 已断开')
                        break
                    print(f'收到客户端 {client_address} 的消息：{data}')

                    # 发送回复
                    reply = input('请输入回复（输入 bye 断开连接）：')
                    client_socket.send(reply.encode('utf-8'))
                    if reply.lower() == 'bye':
                        print(f'客户端 {client_address} 已断开')
                        break
            finally:
                client_socket.close()
                print(f'客户端 {client_address} 已断开')

    finally:
        server_socket.close()
        print('服务器已关闭')


if __name__ == '__main__':
    start_server()
