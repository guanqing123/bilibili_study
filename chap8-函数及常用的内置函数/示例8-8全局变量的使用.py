"""
全局变量

定义：在函数外定义的变量或函数内部使用 global 关键字修饰的变量
作用范围：整个程序，程序运行结束，全局变量的生命周期才结束
"""
a = 100  # 全局变量


def calc(x, y):
    return a + x + y


print(a)  # 100
print(calc(10, 20))  # 130
print('-' * 30)


def calc2(x, y):
    a = 200  # 局部变量，局部变量的名称和全局变量的名称相同
    return a + x + y  # a是局部变量还是全局变量呢？ 局部变量 ，当全局变量和局部变量的名称相同时，优先级高呢？局部变量


print(calc2(10, 20))  # 230
print(a)  # 100
print('-' * 30)


def calc3(x, y):
    global s  # s是在函数中定义的变量,但是使用了global关键字声明，这个变量s变成了全局变量
    s = 300  # 声明和赋值，必须是分开执行
    return s + x + y


print(calc3(10, 20))  # 330
print(s)  # 300
