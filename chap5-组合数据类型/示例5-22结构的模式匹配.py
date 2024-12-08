"""
Python3.11 新特性
1) 结构模型匹配
语法结构如下：
match data:
    case {}:
        pass
    case []:
        pass
    case():
        pass
    case_:
        pass
"""
data = eval(input('请输入要匹配的数据:'))
match data:
    case {'name': 'ysj', 'age': 20}:
        print('字典')
    case [10, 20, 30]:
        print('列表')
    case (10, 20, 40):
        print('元组')
    case _:
        print('相当于多重if中的else')
