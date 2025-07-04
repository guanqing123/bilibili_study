class FatherA:
    def __init__(self, name):
        self.name = name

    def showA(self):
        print('父类A中的方法')


class FatherB:
    def __init__(self, age):
        self.age = age

    def showB(self):
        print('父类中B的方法')


# 多继承
class Son(FatherA, FatherB):
    def __init__(self, name, age, gender):
        FatherA.__init__(self, name)
        FatherB.__init__(self, age)
        self.gender = gender


son = Son('陈梅梅', 20, '女')  # 调用Son类中的__init__执行
son.showA()  # 父类A中的方法
son.showB()  # 父类B中的方法
