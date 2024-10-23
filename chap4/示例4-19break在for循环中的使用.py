for i in 'hello':
    if i == 'e':
        break
    print(i)
print('-' * 3)

for i in range(3):
    user_name = input('请输入您的用户名:')
    pwd = input('请输入密码:')
    if user_name == 'ysj' and pwd == '888888':
        print('系统正在登录,请稍后...')
        break
    else:
        if i < 2:
            print('您还剩余', 2 - i, '次机会')
else:
    print('三次均输入错误')
