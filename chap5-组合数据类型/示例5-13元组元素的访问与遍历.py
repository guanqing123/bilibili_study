t = ('python', 'hello', 'world')
# 根据索引访问元组
print('通过索引t[0]访问元组', t[0])
t2 = t[0:3:2]  # 元组支持切片操作
print('通过切片t[0:3:2]访问元组', t2)

# 元组的遍历
print('-' * 10, '通过for循环遍历元组', '-' * 10)
for item in t:
    print(item)

print('-' * 10, '通过for+range+len()遍历元组', '-' * 10)
# for+range()+len()
for i in range(len(t)):
    print(i, t[i])

print('-' * 10, '通过for+enumerate()遍历元组', '-' * 10)
# 使用enumerate()
for index, item in enumerate(t):
    print(index, '---->', item)

print('-' * 10, '通过for+enumerate()+start()遍历元组', '-' * 10)
for index, item in enumerate(t, start=11):  # 序号从11开始
    print(index, '---->', item)
