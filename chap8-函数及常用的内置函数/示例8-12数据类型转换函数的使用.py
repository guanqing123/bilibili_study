"""
函数名称            描述说明
bool(obj)       获取指定对象 obj 的布尔值
str(obj)        将指定对象 obj 转成字符串类型
int(x)          将 x 转成 int 类型
float(x)        将 x 转成 float 类型
list(sequence)  将序列转成列表类型
tuple(sequence) 将序列转成元组类型
set(sequence)   将序列转成集合类型
"""
print('非空字符串的布尔值:', bool('hello'))  # True
print('空字符串的布尔值:', bool(''))  # 空字符串不是空格字符串 False
print('空列表的布尔值:', bool([]))  # False
print('空列表的布尔值:', bool(list()))  # False
print('空元组的布尔值:', bool(()))  # False
print('空元组的布尔值:', bool(tuple()))  # False
print('空集合的布尔值:', bool(set()))  # False
print('空字典的布尔值:', bool({}))  # False
print('空字典的布尔值:', bool(dict()))  # False
print('-' * 30)
print('非0数值型的布尔值:', bool(123))  # True
print('整数0的布尔值:', bool(0))  # False
print('浮点数0.0的布尔值:', bool(0.0))  # False

# 将其它类型转成字符串类型
lst = [10, 20, 30]
print(type(lst), lst)  # <class 'list'> [10, 20, 30]

s = str(lst)
print(type(s), s)  # <class 'str'> [10, 20, 30]

# float类型和str类型转成int类型
print('-' * 30, 'float类型和str类型转成int类型', '-' * 30)
print(int(98.7) + int('90'))  # 188
# 注意事项
# print(int('98.7')) # ValueError: invalid literal for int() with.txt base 10: '98.7'
# print(int('a')) # ValueError: invalid literal for int() with.txt base 10: 'a'

print('-' * 30, 'int,str类型转成float类型', '-' * 30)
print(float(90) + float('3.14'))  # 93.14

s = 'hello'
print(list(s))  # ['h', 'e', 'l', 'l', 'o']

seq = range(1, 10)
print(tuple(seq))  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(set(seq))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(list(seq))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
