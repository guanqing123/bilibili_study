import os.path


def create_dir(path, num):
    for i in range(1, num + 1):
        dir_name = os.path.join(path, str(i))
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)


if __name__ == '__main__':
    path = 'new_dir'
    if not os.path.exists(path):
        os.mkdir(path)

    num = eval(input('请输入要创建目录的个数:'))
    create_dir(path, num)
