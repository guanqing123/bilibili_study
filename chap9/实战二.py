class Student:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def info(self):
        print(f'{self.name} \t{self.age} \t{self.gender} \t{self.score}')


print('请输入5位学生信息:(姓名#年龄#性别#成绩)')
# result = list()
result = []
for i in range(1, 6):
    str = input(f'请输入第{i}位学生信息及成绩:')
    lst = str.split('#')
    stu = Student(lst[0], lst[1], lst[2], lst[3])
    result.append(stu)

for item in result:
    item.info()

# gq#10#男#99
# cl#11#女#98
# gxy#9#男#97
# gxy#8#女#96
# xcl#7#女#95
