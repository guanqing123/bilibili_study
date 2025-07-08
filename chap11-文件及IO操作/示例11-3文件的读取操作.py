def my_read(filename):
    # (1)打开
    file = open(filename, 'w+', encoding='utf-8')
    # (2)操作
    file.write('你好啊')  # 写入完成,文件的指针在最后
    # seek 修改文件指针的位置
    file.seek(0)
    # 读取
    # s = file.read()  # 读取全部 你好啊
    # s = file.read(2)  # 你好 2指的是2个字符 你好
    # s = file.readline()  # 读取一行数据 你好啊
    # s = file.readline(2) # 读取一行中的2个字符 你好
    # s = file.readlines()  # 读取所有,一行为列表中的一个元素,s是列表 ['你好啊']
    file.seek(3)  # 3个字节,一个中文占三个字节,utf-8
    s = file.read() # 好啊
    print(type(s), s) # <class 'str'> 好啊


if __name__ == '__main__':
    my_read('d.txt')
