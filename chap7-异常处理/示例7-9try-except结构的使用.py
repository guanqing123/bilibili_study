"""
Python 中的异常处理

try...except 的语法结构为：
try:
    可能会抛出异常的代码
except 异常类型 :
    异常处理代码（报错后执行的代码）
"""

try:
    num1 = int(input('请输入一个整数:'))
    num2 = int(input('请输入另一个整数'))
    result = num1 / num2
    print('结果:', result)
except ZeroDivisionError:
    print('除数为0')
