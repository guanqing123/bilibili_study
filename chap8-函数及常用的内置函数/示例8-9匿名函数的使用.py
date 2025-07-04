"""
匿名函数lambda

是指没有名字的函数，这种函数只能使用一次，一般是在函数的函数体只有一句代码且只有一个返回值时，可以使用匿名函数来简化

语法结构：
    result=lambda 参数列表 : 表达式
"""


def calc(a, b):
    return a + b


print(calc(10, 20))

# 匿名函数
s = lambda a, b: a + b  # s表示就是一个匿名函数
print(type(s))  # <class 'function'>
# 调用匿名函数
print(s(10, 20))  # 30
print(s(20, 30))  # 50
print('-' * 30)
# 列表的正常取值操作
lst = [10, 20, 30, 40, 50]
for i in range(len(lst)):
    print(lst[i])
print('-' * 30)

for i in range(len(lst)):
    result = lambda x: x[i]  # 根据索引取值 ,result是的类型是function  ,x是形式参数
    print(result(lst))  # lst是实际参数

#
student_scores = [
    {'name': '陈梅梅', 'score': 98},
    {'name': '王一一', 'score': 95},
    {'name': '张天乐', 'score': 100},
    {'name': '白雪儿', 'score': 65}
]
# 对列表进行排序， 排序的规则 是字典只的成绩
student_scores.sort(key=lambda x: x.get('score'), reverse=True)  # 降序
print(student_scores)
