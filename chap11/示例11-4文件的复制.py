def copy(src, dest):
    origin = open(src, 'r', encoding='utf-8')
    s = origin.read()
    target = open(dest, 'w', encoding='utf-8')
    target.write(s)

    target.close()
    origin.close()


def copy(src, new_path):
    # 文件的复制就是边读边写操作
    # (1)打开源文件
    file1 = open(src, 'rb')
    # (2)打开目标文件
    file2 = open(new_path, 'wb')
    # (3)开始复制,边读边写
    s = file1.read()  # 源文件读取所有
    file2.write(s)  # 向目标文件写入所有

    # (4)关闭
    file2.close()
    file1.close()  # 先打开的后关,后打开的先关


if __name__ == '__main__':
    # copy('d.txt', 'e.txt')
    # ..表示的是上级目录,相当于windows后退, .代表的是当前目录
    copy('../chap10/google.jpg', 'google-copy.jpg')
    print('文件复制完毕。。。')