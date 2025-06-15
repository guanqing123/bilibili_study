"""
2）内置函数 sorted()
sorted(iterable,key=None,reverse=False)
iterable: 表示的是排序的对象
"""
lst = [4, 56, 3, 78, 40, 56, 89]
print('原列表:', lst, id(lst))  # [4, 56, 3, 78, 40, 56, 89] 4386972032
# 排序
asc_lst = sorted(lst)
print('升序:', asc_lst, id(asc_lst))  # [3, 4, 40, 56, 56, 78, 89] 4386871744
print('原列表:', lst, id(lst))  # [4, 56, 3, 78, 40, 56, 89] 4386972032

# 降序
desc_lst = sorted(lst, reverse=True)
print('降序:', desc_lst)  # [89, 78, 56, 56, 40, 4, 3]
print('原列表:', lst)  # [4, 56, 3, 78, 40, 56, 89]

lst2 = ['banana', 'apple', 'Cat', 'Orange']
print('原列表：', lst2)  # ['banana', 'apple', 'Cat', 'Orange']

# 忽略大小写进行排序
new_lst2 = sorted(lst2, key=str.lower)
print('原列表:', lst2)  # ['banana', 'apple', 'Cat', 'Orange']
print('排序后的列表:', new_lst2)  # ['apple', 'banana', 'Cat', 'Orange']
