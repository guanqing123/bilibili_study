"""
try...except...else...finally 的语法结构为：
try:
    可能会抛出异常的代码
except 异常类型 :
    异常处理代码（报错后执行的代码）
else:
    没有抛异常要执行的代码
finally:
    无论是否产生异常都要执行的代码
"""
try:
    num1 = int(input('请输入一个整数:'))
    num2 = int(input('请输入另一个整数'))
    result = num1 / num2

except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')
else:
    print('结果:', result)
finally:
    print('程序执行结束！')
