"""
程序跳转语句 break 用于跳（退）出循环结构，通常与 if 一起搭配使用

语法结构
while 表达式1:
    执行代码
    if 表达式2:
        break
"""
s = 0  # 存储累加和
i = 1  # (1)初始化变量
while i < 11:  # (2)条件判断
    # (3)语句块
    s += i
    if s > 20:
        print('累加和大于20的当前数是:', i)
        break
    i += 1  # (4) 改变变量

print('-' * 20)
i = 0
while i < 3:
    user_name = input('请输入用户名:')
    pwd = input('请输入密码:')
    if user_name == 'ysj' and pwd == '888888':
        print('系统正在登录,请稍后...')
        break
    else:
        if i < 2:
            print('您还剩余', 2 - i, '次机会')
    i += 1
else:
    print('三次均输入错误')
