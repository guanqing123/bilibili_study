"""
Python3.11 新特性
3) 同步迭代
语法结构如下:
match data1,data2:
    case data1,dat2:
        pass
"""
fruits = ['apple', 'orange', 'pear', 'grape']
counts = [10, 3, 4, 5]
for f, c in zip(fruits, counts):
    match f, c:
        case 'apple', 10:
            print('10个苹果')
        case 'orange', 3:
            print('3个桔子')
        case 'pear', 4:
            print('4个梨')
        case 'grape', 5:
            print('5串葡萄')
        case _, _:
            print('其他水果')
