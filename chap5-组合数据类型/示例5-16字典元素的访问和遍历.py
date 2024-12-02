"""
注意事项：字典中的 key 是无序的， Python3.5 及其之前的版本字典的 key 在输出时无序，
但是从 Python3.6 版本之后 Python解释器进行了处理，所以才会看到输出的顺序与添加的顺序“一致”

字典元素的取值：d[key] 或 d.get(key)
"""

d = {'hello': 10, 'world': 20, 'python': 30}
# 访问字典中的元素
# (1)使用d[key]
print(d['hello'])
# (2)d.get(key)
print(d.get('hello'))

# 二者之间是有区别的，如果key不存在，d[key]报错d.get(key)可以指定默认值
# print(d['java']) # KeyError: 'java'
print(d.get('java'))  # None
print(d.get('java', '不存在'))

"""
字典元素的遍历：
1) 遍历出 key 与 value 的元组
for element in d.items():
    pass
"""

print('-'*10, '遍历出 key 与 value 的元组', '-'*10)
# 字典的遍历
for item in d.items():
    print(item, type(item))  # key=value组成的一个元素
    for i in item:
        print(i, end='\t')
    print()


"""
2) 分别遍历出 key 和 value
for key,value in d.items():
    pass
"""
print('-'*10, '在使用for循环遍历时，分别获取key,value', '-'*10)
# 在使用for循环遍历时，分别获取key,value
for key, value in d.items():
    print(key, '--->', value)
