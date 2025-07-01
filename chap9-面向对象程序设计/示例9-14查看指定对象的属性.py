"""
object是所有类直接或间接的父类
所有类都拥有object类的属性和方法

object类中特殊的方法       功能
    __new__()           由系统调用,用于创建对象
    __init__()          创建对象时手动调用,用于初始化对象属性值
    __str__()           对象的描述,返回值是str类型,默认输出对象的内存地址
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好,我叫:{self.name},我今年:{self.age}')


# 创建Person类的对象
per = Person('陈梅梅', 20)  # 创建对象的时候会自动调用__init__方法()
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'show']
print(dir(per))

print(per)  # 自动调用了__str__方法 <__main__.Person object at 0x103d558b0>
