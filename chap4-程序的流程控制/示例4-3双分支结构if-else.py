"""
双分支结构 if...else... 语法结构

if 表达式:
    语句 1
else:
    语句 2
"""
number = eval(input('请输入您的6位中奖号码：'))
# if...else
if number == 987654:
    print('恭喜您中奖了!')
else:
    print('您未中本期大奖!')

print('-' * 5 + '以上代码可以使用条件表达式进行简化' + '-' * 5)

result = '恭喜您中奖了!' if number == 987654 else '您未中本期大奖!'
print(result)

print('恭喜您中奖了!' if number == 987654 else '您未中本期大奖!')
