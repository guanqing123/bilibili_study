d = {1001: '李梅', 1002: '王华', 1003: '张峰'}
print(d, id(d))

# 向字典中添加元素
d[1004] = '张丽丽'  # 直接使用赋值运算符向字典中添加元素
print(d, id(d))

# 获取字典中所有的key
keys = d.keys()
print(keys, type(keys))  # dict_keys([1001, 1002, 1003, 1004])
print(list(keys))
print(tuple(keys))

# 获取字典中所有的value
values = d.values()
print(values)  # dict_values(['李梅', '王华', '张峰', '张丽丽'])
print(list(values))
print(tuple(values))

# 如果将字典中的数据转成key-value的形式,以元组的方式进行展现
lst = list(d.items())
print(lst)

d = dict(lst)
print(d)

# 使用pop函数
print(d.pop(1001))
print(d)

"""
d.pop(key,default): key 存在获取相应的 value ，同时删除 key-value 对，否则获取默认值
"""
print(d.pop(1008, '不存在'))

"""
d.popitem(): 随机从字典中取出一个 key-value 对，结果为元组类型，同时将该key-value 从字典中删除
"""
# 随机删除
print(d.popitem())
print(d)

# 清空字典中所有的元素
d.clear()
print(d)
# Python中一切皆对象，每个对象都有一个布尔值
print(bool(d))  # 空字典的布尔值为False
