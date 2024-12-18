# 位运算符 把数字看作二进制数来进行计算的

print('按位与运算：', 12 & 8)  # 8
print('按位或运算：', 4 | 8)  # 12
print('按位异或运算符：', 31 ^ 22)  # 9 位上相同则为0,位上不同则为1
print('按位取反：', ~123)  # -124

print('左移位：', 2 << 2)  # 8 表示的是2向左移动两位  2*2*2
print('左移位：', 2 << 3)  # 16 相当于 2* 2*2*2
print('右移位：', 8 >> 2)  # 8向右移动两位相当于 8//2, 4//2
print('右移位：', -8 >> 2)  # -2
