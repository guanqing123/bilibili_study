"""
for...else...结构
for 循环变量 in 遍历对象:
    语句块1
else:
    语句块2
"""
s = 0  # 用于存储累加和
for i in range(1, 11):
    s += i
else:
    print('1-10之间的累加和为:', s)
