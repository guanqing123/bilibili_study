"""
列表的方法                   描述说明
lst.append(x)           在列表 lst 最后增加一个元素
lst.insert(index,x)     在列表中第 index 位置增加一个元素
lst.clear()             清除列表 lst 中所有元素
lst.pop(index)          将列表 lst 中第 index 位置的元素取出，并从列表中将其删除
lst.remove(x)           将列表 lst 中出现的第一个元素 x 删除
lst.reverse(x)          将列表 lst 中的元素反转
lst.copy()              拷贝列表 lst 中的所有元素，生成一个新的列表
"""

lst = ['hello', 'world', 'python']
print('原列表：', lst, id(lst))
# 增加元素的操作
lst.append('sql')
print('增加元素之后：', lst, id(lst))

# 使用insert(index,x)在指定的index位置上插入元素x
lst.insert(1, 100)
print(lst, id(lst))

# 列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表:', lst, id(lst))

# 使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1), lst, id(lst))

# 清除列表中所有的元素clear()
# lst.clear()
# print(lst,id(lst))

# 列表的反向
lst.reverse()  # 不会产生新的列表，在原列表的基础上进行的
print(lst)

# 列表的拷贝，将产生一个新的列表对象
new_lst = lst.copy()
print(lst, id(lst))
print(new_lst, id(new_lst))

# 列表元素的修改操作
# 根据索引进行修改元素
lst[1] = 'mysql'
print(lst)
