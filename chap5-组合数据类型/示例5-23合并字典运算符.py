"""
Python3.11 新特性
2) 字典合并运算符 |
"""
d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40, 'e': 50}
merged_dict = d1 | d2
print(merged_dict)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
