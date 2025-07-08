# 存储和读取一纬数组
def my_write():
    # 一维数据, 可以使用列表, 元组, 或集合
    lst = ['张三', '李四', '王五', '陈六', '麻七']
    with open('student.csv', 'w') as file:
        file.write(','.join(lst))  # 将列表转成字符串


def my_read():
    with open('student.csv', 'r') as file:
        s = file.read()
        lst = s.split(',')
        print(type(lst), lst)


# 存储和读取二维数据
def my_write_table():
    lst = [
        ['商品名称', '单价', '采购数量'],
        ['水杯', '98.5', '20'],
        ['鼠标', '89', '100']
    ]
    with open('table.csv', 'w', encoding='utf-8') as file:
        for item in lst:
            file.write(','.join(item))
            file.write('\n')


def my_read_table():
    with open('table.csv', 'r', encoding='utf-8') as file:
        result = []
        lst = file.readlines()
        for item in lst:  # item是字符串类型
            tp = item[:len(item)-1].split(',')  # 字符串切片,把\n去掉
            result.append(tp)
    print(result)


if __name__ == '__main__':
    # my_write()
    # my_read()
    my_write_table()
    my_read_table()
