"""
函数名称                     描述说明
sorted(iter)            对可迭代对象进行排序
reversed(sequence)      反转序列生成新的迭代器对象
zip(iter1,iter2)        将 iter1 与 iter2 打包成元组并返回一个可迭代的 zip 对象
enumerate(iter)         根据 iter 对象创建一个 enumerate 对象
all(iter)               判断可迭代对象 iter 中所有元素的布尔值是否都为 True
any(iter)               判断可迭代对象 iter 中所有元素的布尔值是否都为 False
next(iter)              获取迭代器的下一个元素
filter(function,iter)   通过指定条件过滤序列并返回一个迭代器对象
map(function,iter)      通过函数 function 对可迭代对象 iter 的操作返回一个迭代器对象
"""
print('*' * 20, 'sorted', '*' * 20)
lst = [54, 56, 77, 4, 567, 34]
# (1)排序操作
asc_lst = sorted(lst)  # 升序
desc_lst = sorted(lst, reverse=True)  # 降序
print('原列表:', lst, id(lst))
print('升序:', asc_lst, id(asc_lst))
print('降序:', desc_lst, id(desc_lst))

print('*' * 20, 'reversed', '*' * 20)
# （2）reversed 反向
new_lst = reversed(lst)
print(lst, id(lst))
print(new_lst, type(new_lst))  # <class 'list_reverseiterator'> 迭代器对象
print(list(new_lst), id(new_lst))

print('*' * 20, 'zip', '*' * 20)
# (3)zip
x = ['a', 'b', 'c', 'd']
y = [10, 20, 30, 40, 50]
zipobj = zip(x, y)
print(type(zipobj))  # <class 'zip'>
print(list(zip(x, y)), dict(zip(x, y)), tuple(zip(x, y)))

print('*' * 20, 'enumerate', '*' * 20)
# (4)enumerate
enum = enumerate(y, start=1)
print(type(enum))  # <class 'enumerate'>
print(tuple(enum), list(enumerate(y, start=1)), dict(enumerate(y, start=2)))

print('*' * 20, 'all', '*' * 20)
# (5)all
lst2 = [10, 20, '', 30]
print(all(lst2))  # False  ,空字符串的布尔值是False
print(all(lst))  # True

print('*' * 20, 'any', '*' * 20)
# (6)any
print(any(lst2))  # True

print('*' * 20, 'next', '*' * 20)
# (7)
print(next(zipobj))  # ('a', 10)
print(next(zipobj))
print(next(zipobj))

print('*' * 20, 'filter', '*' * 20)


def fun(num):
    return num % 2 == 1  # 可能是True，False


obj = filter(fun, range(10))  # 将range(10),0-9的整数，都执行一次fun操作
print(list(obj))  # [1, 3, 5, 7, 9]

print('*' * 20, 'map', '*' * 20)


def upper(x):
    return x.upper()


new_lst2 = ['hello', 'world', 'python']
obj2 = map(upper, new_lst2)
print(list(obj2))
