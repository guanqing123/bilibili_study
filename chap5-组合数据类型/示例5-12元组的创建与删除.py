"""
元组：是Python中内置的不可变序列
元组：在Python中使用 () 定义元组，元素与元素之间使用英文的逗号分隔
元组中只有一个元素的时候，逗号也不能省略

元组的创建方式有两种:
1) 使用 () 直接创建元组
语法结构如下：
元组名 =(element1,element2,......elementN)

2) 使用内置函数 tuple() 创建元组
语法结构如下：
元组名 =tuple(序列)

删除元组：
del 元组名
"""

# 使用小括号创建元组
t = ('hello', [10, 20, 30], 'python', 'world')
print(t)  # ('hello', [10, 20, 30], 'python', 'world')

# 使用内置函数tuple()创建元组
t = tuple('helloworld')
print(t)  # ('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')

t = tuple([10, 20, 30, 40])
print(t)  # (10, 20, 30, 40)
t2 = (50, 60)
newt = t.__add__(t2)
print(t, t2, newt)  # (10, 20, 30, 40) (50, 60) (10, 20, 30, 40, 50, 60)

print('10在元组中是否存在：', (10 in t))  # True
print('10在元组是不存在:', (10 not in t))  # False
print('最大值:', max(t))  # 40
print('最小值:', min(t))  # 10
print('len:', len(t))  # 4
print('t.index:', t.index(10))  # 0
print('t.count', t.count(10))  # 1

# 如果元组中只有一个元素
t = (10)
print(t, type(t))  # 10 <class 'int'>

# 如果元组中只有一个元素，逗号不能省
y = (10,)
print(y, type(y))  # (10,) <class 'tuple'>

# 元组的删除
del t
# print(t) # NameError: name 't' is not defined
