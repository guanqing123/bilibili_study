"""
字典生成式
d={ key:value for item in range }
d={key:value for key,value in zip(lst1,lst2)}
"""

import random

d = {item: random.randint(1, 100) for item in range(4)}
print(d)  # {0: 61, 1: 98, 2: 25, 3: 67}

# 创建两个列表
lst = [1001, 1002, 1003]
lst2 = ['陈梅梅', '王一一', '李丽丽']
d = {key: value for key, value in zip(lst, lst2)}
print(d)  # {1001: '陈梅梅', 1002: '王一一', 1003: '李丽丽'}
