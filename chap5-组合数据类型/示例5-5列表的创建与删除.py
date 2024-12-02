"""
列表是指一系列的按特定顺序排列的元素组成。
列表是 Python 中内置的可变序列
列表在 Python 中使用 [] 定义列表，元素与元素之间使用英文的逗号分隔
列表中的元素可以是任意的数据类型
"""

# 列表的创建方式有两种
# 1）直接使用[]创建列表
# 语法结构：列表名 =[element1,element2,......elementN]
lst = ['hello', 'world', 98, 100.5]
print(lst[0:3:2])
print('lst=', lst)

# 2）使用内置的函数list()创建列表
# 语法结构如下：列表名 =list( 序列 )
lst2 = list('helloworld')
lst3 = list(range(1, 10, 2))  # 从1开始到10结束，步长为2，不包含10
print('lst2=', lst2)
print('lst3=', lst3)

# 列表是序列中的一种，对序列的操作符，运算符，函数均可以使用
print('序列中 lst + lst2 + lst3 操作:', lst + lst2 + lst3)  # 序列中的相加操作
print('序列中 lst * 3 操作:', lst * 3)  # 序列的相乘操作
print('len(lst):', len(lst))
# print('max(lst):', max(lst)) TypeError: '>' not supported between instances of 'int' and 'str'
print('max(lst2):', max(lst2))
print('max(lst3):', max(lst3))
print('min(lst3):', min(lst3))

print('lst2.count(o):', lst2.count('o'))  # 统计o的个数
print('lst2.index(o):', lst2.index('o'))  # o在列表lst2中第一次出现的位置

# 列表的删除操作
# 语法结构如下: del 列表名
lst4 = [10, 20, 30]
print(lst4)
# 删除列表
del lst4
# print(lst4) # NameError: name 'lst4' is not defined. Did you mean: 'lst'?
