score = input('请输入成绩等级：')
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('中等')
    case 'D':
        print('及格')
    case 'E':
        print('不及格')

score = eval(input('请输入成绩：'))
match score:
    case x if x >= 90:
        print('优秀')
    case x if x >= 80:
        print('良好')
    case x if x >= 70:
        print('中等')
    case x if x >= 60:
        print('及格')
    case _:
        print('不及格')