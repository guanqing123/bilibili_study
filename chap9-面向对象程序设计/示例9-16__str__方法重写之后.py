class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'这是一个人类,具有name和age两个实例属性,name:{self.name},age:{self.age}'  # 返回值是一个字符串


# 创建Person类的对象
per = Person('陈梅梅', 20)
print(per)  # 还是内存地址吗？不是,__str__方法中的内容 直接输出对象名,实际上是调用__str__方法
print(per.__str__())  # 手动调用
