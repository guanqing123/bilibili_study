"""
字典类型是根据一个信息查找另一个信息的方式构成了“键值对”，它表示索引用的键和对应的值构成的成对关系

字典类型的创建方式
第一种使用 {} 直接创建字典 d={key1:value1,key2:value2......}

第二种使用内置函数 dict() 创建字典
1) 通过映射函数创建字典
zip(lst1,lst2)
"""
# (1)创建字典
d = {10: 'cat', 20: 'dog', 30: 'pet', 20: 'zoo'}
print(d)  # key相同时，value值进行了覆盖

# (2)zip函数
lst1 = [10, 20, 30, 40]
lst2 = ['cat', 'dog', 'pet', 'zoo', 'car']
zipobj = zip(lst1, lst2)
print(zipobj)  # <zip object at 0x000001ECD5A24F00>
# print(list(zipobj)) # [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
d = dict(zipobj)
print(d)  # {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}
print(d.get(30), d.get('30'))

# 使用参数创建字典
d = dict(cat=10, dog=20)  # 左侧cat是key ,右侧的是value
print(d)

t = (10, 20, 30)
print({t: 10})  # t是key,10是value ,元组是可以作为字典中的key

# lst=[10,20,30]
# print({lst:10}) # TypeError: unhashable type: 'list'

# 字典属于序列
print('max:', max(d))
print('min:', min(d))
print('len:', len(d))
# 字典的删除
del d
# print(d)
