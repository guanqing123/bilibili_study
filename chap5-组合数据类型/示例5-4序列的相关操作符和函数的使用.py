"""
操作符 / 函数          描述说明
x in s            如果 x 是 s 的元素，结果为 True ，否则结果为 False
x not in s        如果 x 不是 s 的元素，结果为 True ，否则结果为 False
len(s)            序列 s 中元素的个数 (即序列的长度)
max(s)            序列 s 中元素的最大值
min(s)            序列 s 中元素的最小值
s.index(x)        序列 s 中第一次出现元素 x 的位置
s.count(x)        序列 s 中出现 x 的总次数
"""

s = 'helloworld'
print('e在helloworld中存在吗?', ('e' in s))  # in的使用
print('v在helloworld中存在吗?', ('v' in s))
# not in 的使用

print('e在helloworld中不存在吗?', ('e' not in s))  # not in的使用
print('v在helloworld中不存在吗?', ('v' not in s))

# 内置函数的使用
print('len():', len(s))
print('max():', max(s))
print('min():', min(s))

# 序列对象的方法，使用序列的名称，打点调用
print('s.index():', s.index('o'))  # o在s中第一次出现的索引位置 4
# print('s.index():', s.index('v'))  # ValueError: substring not found ,报错的原因是v在字符串中根本不存在，不存在所以找不到
print('s.count():', s.count('o'))  # 统计o在字符串s中出现的次数
