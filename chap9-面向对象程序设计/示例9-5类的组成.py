"""
类属性     直接定义在类中,方法外的变量
实例属性    定义在__init__方法中,使用self打点的变量
实例方法    定义在类中的函数,而且自带参数self
静态方法    使用装饰器@staticmethod修饰的方法
类方法      使用装饰器@classmethod修饰的方法
"""


class Student:
    # 类属性：定义在类中,方法外的变量
    school = '北京XXX教育'

    # 初始化方法
    def __init__(self, xm, age):  # xm,age是方法的参数,是局部变量,xm,age的作用域是整个__init__方法
        self.name = xm  # =号左侧是实例属性,xm是局部变量,将局部变量的值xm赋值给实例属性self.name
        self.age = age  # 实例的名称和局部变量的名称可以相同

    # 定义在类中的函数,称为方法,自带一个参数self
    def show(self):
        print(f'我叫:{self.name},今年:{self.age}岁了')

    # 静态方法
    @staticmethod
    def sum():
        # print(self.name)
        # self.show()
        print('这是一个静态方法,不能调用实例属性,也不能调用实例方法')

    # 类方法
    @classmethod
    def cm(cls):  # cls -->class的简写
        # print(self.name)
        # self.show()
        print('这是一个类方法,不能调用实例属性,也不能调用实例方法')


# 创建类的对象
stu = Student('ysj', 28)  # 为什么传了两个参数,因为__init__方法中,有两个行参,self是自带的参数,无需手动传入
# 实例属性,使用对象名进行打点调用的
print(stu.name, stu.age)  # ysj 28
# 类属性,直接使用类名打点调用
print(Student.school, stu.school)  # 北京XXX教育 北京XXX教育

# 实例方法,使用对象名进行打点调用
stu.show()  # 我叫:ysj,今年:28岁了

# 类方法,@classmethod进行修饰的方法,直接使用类名打点调用
Student.cm()  # 这是一个类方法,不能调用实例属性,也不能调用实例方法
stu.cm()  # 这是一个类方法,不能调用实例属性,也不能调用实例方法

# 静态方法,@staticmethod进行修饰的方法,直接使用类名打点调用
Student.sum()  # 这是一个静态方法,不能调用实例属性,也不能调用实例方法
stu.sum()  # 这是一个静态方法,不能调用实例属性,也不能调用实例方法
