while True:
    print('-' * 10, '欢迎使用10086查询功能', '-' * 10)
    print('1.查询当前余额')
    print('2.查询当前的剩余流量')
    print('3.查询当前的剩余通话时长')
    print('0.退出系统')
    num = eval(input('请输入您的数字:'))
    if num == 1:
        print('余额:', 88)
    elif num == 2:
        print('剩余流量:', '20G')
    elif num == 3:
        print('剩余通话:', 20, '分钟')
    elif num == 0:
        break
    else:
        print('对不起,您的输入有误,请重新输入')
else:
    print('程序退出')