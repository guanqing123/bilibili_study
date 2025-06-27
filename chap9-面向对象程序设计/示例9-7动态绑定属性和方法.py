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


# 创建两个Student类型的对象
gq = Student('gq', 35)
cl = Student('cl', 34)
print(gq.name, gq.age)  # gq 35
print(cl.name, cl.age)  # cl 34

# 为gq动态绑定一个属性
gq.gender = '男'
print(gq.name, gq.age, gq.gender)  # gq 35 男


# print(cl.gender)  # AttributeError: 'Student' object has no attribute 'gender'
# 动态绑定方法
def introduce():
    print('我是一个普通的函数,我被动态绑定了gq对象的方法')


gq.fun = introduce  # 函数的赋值
# fun就是gq对象的方法
# 调用
gq.fun() # 我是一个普通的函数,我被动态绑定了gq对象的方法
