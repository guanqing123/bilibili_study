"""
enumerate 函数的使用语法结构
for index ,item in enumerate(lst):
    输出 index 和 item
"""

print('*'*10, '使用for循环遍历列表元素', '*'*10)
lst = ['hello', 'world', 'python', 'php']
# 使用遍历循环for遍历列表元素
for item in lst:
    print(item)

print('*'*10, '使用for循环遍历索引和元素', '*'*10)
# 使用for循环,range()函数，len()函数，根据索引进行遍历
for i in range(0, len(lst)):
    print(i, '-->', lst[i])

print('*'*10, '使用for循环加enumerate函数', '*'*10)
# 第三种遍历方式 enumerate()函数
for index, item in enumerate(lst):
    print(index, item)  # index是序号，不是索引

print('*'*10, '使用for循环加enumerate函数，手动修改序号的起始值', '*'*10)
# 手动修改序号的起始值
for index, item in enumerate(lst, start=1):  #
    print(index, item)

print('*'*10, '使用for循环加enumerate函数，省略start不写，直接写起始值', '*'*10)
for index, item in enumerate(lst, 1):  # 省略start不写，直接写起始值
    print(index, item)
