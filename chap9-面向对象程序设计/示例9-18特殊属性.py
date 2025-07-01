"""
特殊属性                    功能描述
obj.__dict__            对象的属性字典
obj.__class__           对象所属的类
class.__bases__         类的父类元组
class.__base__          类的父类
class.__mro__           类的层次结构
class._subclasses__()   类的子类列表
"""


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建类的对象
a = A()
b = B()
# 创建C类的对象
c = C('陈梅梅', 20)

print('对象a的属性字典:', a.__dict__)  # 对象的属性字典 {}
print('对象b的属性字典:', b.__dict__)  # {}
print('对象c的属性字典:', c.__dict__)  # {'name': '陈梅梅', 'age': 20}

print('-' * 40)
print('对象a所属的类:', a.__class__)  # <class '__main__.A'>
print('对象b所属的类:', b.__class__)  # <class '__main__.B'>
print('对象c所属的类:', c.__class__)  # <class '__main__.C'>

print('-' * 40)
print('A类的父类元组:', A.__bases__)  # (<class 'object'>,)
print('B类的父类元组:', B.__bases__)  # (<class 'object'>,)
print('C类的父类元组:', C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)

print('-' * 40)
print('A类的父类:', A.__base__)  # <class 'object'>
print('B类的父类:', B.__base__)  # <class 'object'>
print('C类的父类:', C.__base__)  # A 类,如果继承了N多个父类,结果只显示第一个父类 <class '__main__.A'>

print('-' * 40)
print('A类的层次结构:', A.__mro__)  # (<class '__main__.A'>, <class 'object'>)
print('B类的层次结构:', B.__mro__)  # (<class '__main__.B'>, <class 'object'>)
# C类继承了A类,B类,间接继承了object类
print('C类的层次结构:', C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

print('-' * 40)
print('A类的子类列表:', A.__subclasses__())  # A的子类有C类 [<class '__main__.C'>]
print('B类的子类列表:', B.__subclasses__())  # [<class '__main__.C'>]
print('C类的子类列表:', C.__subclasses__())  # []列表
