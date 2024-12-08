"""
Python 中的集合与数学中集合的概念一致
Python 中的集合是一个无序的不重复元素序列
集合中只能存储不可变数据类型
在 Python 中集合使用 {} 定义
与列表、字典一样，都是 Python 中的可变数据类型

集合的创建方式有两种:
1) 使用 {} 直接创建集合
语法结构如下：
s={element1,element2,......elementN}
"""
# {}直接创建集合
s = {10, 20, 30, 40}
print(s)
# 集合只能存储不可变数据类型
# s={[10,20],[30,40]} #TypeError: unhashable type: 'list'
# print(s)

"""
2) 使用内置函数 set() 创建集合
语法结构如下：
s=set(可迭代对象)
"""
# 使用set()创建集合
s = set()  # 创建了一个空集合,空集合的布尔值是False
print(s)
s = {}  # 创建的是集合还是字典呢？
print(s, type(s))  # dict

s = set('helloworld')
print(s)

s2 = set([10, 20, 30])
print(s2)

s3 = set(range(1, 10))
print(s3)

# 集合属于序列中的一种
print('max:', max(s3))
print('min:', min(s3))
print('len:', len(s3))

print('9在集合中存在吗？', (9 in s3))
print('9在集合中不存在吗？', (9 not in s3))

"""
集合的删除
语法结构如下:
del 集合名
"""
# 集合的删除操作
del s3
# print(s3)#NameError: name 's3' is not defined. Did you mean: 's'?
