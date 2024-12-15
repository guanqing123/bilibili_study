"""
权限控制：是通过对属性或方法添加单下划线、双下划线以及首尾双下划线来实现
单下划线开头：以单下划线开头的属性或方法表示protected受保护的成员,这类
    成员被视为仅供内部使用,允许类本身和子类进行访问,单实际上它可以被外部
    代码访问。
双下划线开头：表示private私有的成员,这类成员只允许定义该属性或方法的类
    本身进行访问。
首尾双下划线：一般表示特殊的方法。
"""


class Student:
    # 首尾双下划线
    def __init__(self, name, age, gender):
        self._name = name  # self._name受保护的,只能本类和子类访问
        self.__age = age  # self.__age表示私有的,只能类本身去访问
        self.gender = gender  # 普通的实例属性,类的内部,外部,及子类都可以访问

    def _fun1(self):  # 受保护的
        print('子类及本身可以访问')

    def __fun2(self):  # 私有的
        print('只有定义的类可以访问')

    def show(self):
        self._fun1()  # 类本身访问受保护的方法
        self.__fun2()  # 类本身访问私有方法
        print(self._name)  # 受保护的实例属性
        print(self.__age)  # 私有的实例属性


# 创建一个学生类的对象
stu = Student('gq', 34, '男')
# 类的外部
print(stu._name)
# print(stu.__age) # AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?

# 调用受保护的实例方法
stu._fun1()  # 子类及本身可以访问
# 私有方法
# stu.__fun2()  # AttributeError: 'Student' object has no attribute '__fun2'. Did you mean: '_fun1'?

# 私有的实例属性和方法是真的不能访问吗?
print(stu._Student__age)  # 为什么可以这样访问呢？
stu._Student__fun2()

print(dir(stu))
