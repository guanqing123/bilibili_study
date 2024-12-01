"""
列表生成式的语法结构:
lst=[expression for item in range]
lst=[expression for item in range if condition]
"""

import random

lst = [item for item in range(1, 11)]
print(lst)

lst = [item * item for item in range(1, 11)]
print(lst)

lst = [random.randint(1, 100) for _ in range(10)]
print(lst)

# 从列表中选择符合条件的元素组成新的列表
lst = [i for i in range(10) if i % 2 == 0]
print(lst)
