class Student(object):
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 成绩: {self.score}")


lst = []
for i in range(5):
    ins = input("请输入学生姓名,年龄,性别,成绩;用#号进行分隔：")
    name, age, gender, score = ins.split('#')
    stu = Student(name, age, gender, score)
    lst.append(stu)

for stu in lst:
    stu.info()
