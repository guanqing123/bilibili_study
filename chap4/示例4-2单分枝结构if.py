number = eval(input('请输入您的6位中奖号码：'))
# 使用if语句
if number == 987654:  # 等值判断
    print('恭喜您,中奖了！')

if number != 987654:
    print('您未中本期大奖')

print('-----以上if判断的表达式,是通过比较运算符计算出来的,结果是布尔值类型-----')
n = 98  # 赋值操作
if n % 2:  # 98%2的余数是0, 0的布尔值是False, 非0的布尔值位True
    print(n, '是奇数')  # 由于98%2的余数是0, 所以该行代码不执行

if not n % 2:  # 98%2的余数是0, 0的布尔值是False, not False 的结果为True
    print(n, '为偶数')

print('-' * 8 + '判断一个字符串是否是空字符串' + '-' * 8)
x = input('请输入一个字符串：')
if x:  # 在Python中一切皆对象, 每个对象都有一个布尔值, 而非空字符串的布尔值为True, 空字符的布尔值为False
    print('x是一个非空字符串')

if not x:  # 空字符串的布尔值为False, 取反, not False的结果为True
    print('x是一个空字符串')
