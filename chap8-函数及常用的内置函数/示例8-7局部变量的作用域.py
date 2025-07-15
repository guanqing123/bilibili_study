"""
局部变量

定义：在函数定义处的参数和函数内部定义的变量
作用范围：仅在函数内部，函数执行结束，局部变量的生命周期也结束
"""


def calc(a, b):
    s = a + b
    return s


result = calc(10, 20)
print(result)
# print(data,b,s) # data,b是函数的参数，参数是局部变量 ,s是函数中定义的变量，局部变量
