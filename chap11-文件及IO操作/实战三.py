import time


def show_info():
    print('请选择你要的操作, 0.退出,1:显示日志')


def write_log(username):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('用户' + username + ': 于' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '登录系统\n')


if __name__ == '__main__':
    username = input('请输入用户名:')
    password = input('请输入密码:')
    if username == 'admin' and password == '123456':
        write_log(username)
        print('登录成功')
        while True:
            show_info()
            choice = input('请选择:')
            if choice == '0':
                break
            elif choice == '1':
                with open('log.txt', 'r', encoding='utf-8') as file:
                    print(file.read())
    else:
        print('用户名或密码错误')
