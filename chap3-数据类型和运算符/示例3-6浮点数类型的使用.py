height = 187.6  # 身高
print(height)
print(type(height))  # type()查看height这个变量的数据类型 <class 'float'>

x = 10
y = 10.0
print('x的数据类型：', type(x))  # <class 'int'>
print('y的数据类型：', type(y))  # <class 'float'>

x = 1.99E1413
print('科学计算法：', x, 'x的数据类型：', type(x))  # inf(表示无穷大) <class 'float'>
print(0.1 + 0.2)  # 不确定的尾数问题 0.30000000000000004

print(round(0.1 + 0.2, 1))  # 0.3
