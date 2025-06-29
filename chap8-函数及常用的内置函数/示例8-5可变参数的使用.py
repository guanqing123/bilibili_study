"""
可变参数

又分为个数可变的位置参数和个数可变的关键字参数两种:
    1)其中个数可变的位置参数是在参数前加一颗星(*para),para 形式参数的名称，函数调用时可接收任意个数的实际参数，并放到一个元组中。
    2)个数可变的关键字参数是在参数前加两颗星(**para),在函数调用时可接收任意多个 “参数 = 值”形式的参数，并放到一个字典中。
"""


# 个数可变的位置参数
def fun(*para):
    print(type(para), end='\t')
    for item in para:
        print(item, end='\t')
    print()


# 调用
fun(10, 20, 30, 40)  # <class 'tuple'>	10	20	30	40
fun(10)  # <class 'tuple'>	10
fun(20, 30)  # <class 'tuple'>	20	30
# 实际上传递的是一个参数
fun([11, 22, 33, 44])  # <class 'tuple'>	[11, 22, 33, 44]
# 在调用时，参数前加一颗星，分将列表进行解包
fun(*[11, 22, 33, 44])  # <class 'tuple'>	11	22	33	44


# 个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara), end='\t')
    for key, value in kwpara.items():
        print(key, '-----', value, end='\t')
    print()


# 调用关键字参数
fun2(name='娟子姐', age=18, height=170)  # <class 'dict'>	name ----- 娟子姐	age ----- 18	height ----- 170

d = {'name': '娟子姐', 'age': 18, 'height': 170}
# fun2(d) # TypeError: fun2() takes 0 positional arguments but 1 was given

fun2(**d)  # 系列解包操作 <class 'dict'>	name ----- 娟子姐	age ----- 18	height ----- 170
