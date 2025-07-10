import socket


def start_client():
    client_socket = socket.socket()
    client_socket.connect(('localhost', 8899))
    print('已连接到服务器')

    try:
        while True:  # 持续与服务器对话
            # 发送消息
            message = input("请输入消息（输入 'bye' 断开连接）: ")
            client_socket.send(message.encode('utf-8'))
            if message.lower() == 'bye':
                print('客户端主动断开连接')
                break

            # 接收回复
            reply = client_socket.recv(1024).decode('utf-8')
            if not reply or reply.lower() == 'bye':
                print('服务器主动断开连接')
                break
            print(f'收到服务器的回复：{reply}')
    finally:
        client_socket.close()
        print('已断开与服务器的连接')


if __name__ == '__main__':
    start_client()
