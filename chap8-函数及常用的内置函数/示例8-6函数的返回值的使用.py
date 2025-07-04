"""
返回值 return
1)、如果函数的运行结果需要在其它函数中使用，那么这个函数就应该被定义为带返回值的函数。
2)、函数的运行结果使用 return 关键字进行返回
3)、return 可以出现在函数中的任意一个位置，用于结束函数。
4)、返回值可以是一个值，或多个值，如果返回的值是多个，结果是一个元组类型。
"""


# 函数的返回值
def calc(a, b):
    print(a + b)


calc(10, 20)  # 30
print(calc(1, 2))  # 3 None


def calc2(a, b):
    s = a + b
    return s  # 将s返回给函数的调用处去处理


print('-' * 10)
get_s = calc2(1, 2)  # 存储到变量中
print(get_s)

get_s2 = calc2(calc2(1, 2), 3)  # 1+2+3  先去执行calc2(1,2) 返回 结果为3，再去执行calc2(3,3)
print(get_s2)


# 返回值可以是多个
def get_sum(num):
    s = 0  # 累加和
    odd_sum = 0  # 奇数和
    even_sum = 0  # 偶数和
    for i in range(1, num + 1):
        if i % 2 != 0:  # 说明是奇数
            odd_sum += i
        else:
            even_sum += i
        s += i
    return odd_sum, even_sum, s  # 三个值


result = get_sum(10)
print(type(result))  # <class 'tuple'>
print(result)  # (25, 30, 55)

# 解包赋值
a, b, c = get_sum(10)  # 返回3个值，元组类型
print(a)  # 25
print(b)  # 30
print(c)  # 55
