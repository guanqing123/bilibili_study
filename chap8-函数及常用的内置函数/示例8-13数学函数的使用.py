"""
函数名称            描述说明
abs(x)          获取 x 的绝对值
divmod(x,y)     获取 x 与 y 的商和余数
max(sequence)   获取 sequence 的最大值
min(sequence)   获取 sequence 的最小值
sum(iter)       对可迭代对象进行求和运算
pow(x,y)        获取 x 的 y 次幂
round(x,d)      对 x 进行保留 d 位小数，结果四舍五入
"""
print('绝对值:', abs(100), abs(-100), abs(0))  # 100 100 0
print('商和余数:', divmod(13, 4), type(divmod(13, 4)))  # (3, 1) <class 'tuple'>
print('最大值:', max('hello'))  # o
print('最大值:', max([10, 4, 56, 78, 4])) # 78
print('最小值:', min('hello'))  # e
print('最小值:', min([10, 4, 56, 78, 4])) # 4

print('求和:', sum([10, 34, 45])) # 89
print('x的y次幂:', pow(2, 3)) # 8

# 四舍五入
print(round(3.1415926))  # round函数只有一个参数，保留整数 3
print(round(3.9415926))  # 4
print(round(3.1415926, 2))  # 2表示的是保留两位小数 3.14
print(round(314.15926, -1))  # 314 ,-1位，个位进行四舍五入 结果是: 310
print(round(314.15926, -2))  # 314 ,-2,十位进行四舍五入 结果是: 300
