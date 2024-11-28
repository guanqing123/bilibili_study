# 选择结构 也称分支结构，是按照条件选择执行不同的代码段
"""
单分支结构 if 的语法结构

if 表达式:
    语句块
"""
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

print('-' * 10 + '表达式也可以是一个单纯的布尔型变量' + '-' * 10)
flag = eval(input('请输入一个布尔类型的值：True或False'))
if flag:
    print('flag的值为True')

if not flag:
    print('flag的值为False')

print('-' * 10 + '使用if语句时,如果语句块中只有一句代码,可以将语句块直接写中冒号的后面' + '-' * 10)
a = 10
b = 5
if a>b:max = a  # 语句块只有一句的时候,语句直接跟在:后面,赋最大值
print('a和b的最大值为：', max)
