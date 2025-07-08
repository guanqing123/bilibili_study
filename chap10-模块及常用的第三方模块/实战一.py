import prettytable as pt


# 显示座席
def show_ticket(row_num):
    tb = pt.PrettyTable()  # 创建一张表格
    # 设置标题（表格的排头部分）
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    # 遍历有票
    for i in range(1, row_num + 1):
        lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)


# 订票
def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()  # 创建一张表格
    # 设置标题（表格的排头部分）
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(1, row_num + 1):
        lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
        if int(row) == i:
            lst[int(column)] = '已售'
        tb.add_row(lst)
    print(tb)


if __name__ == '__main__':
    row_num = 6

    show_ticket(row_num)

    # 开始售票
    choose_num = input('请输入您选择的座席:如4,3表示第4排第3列:')
    row, column = choose_num.split(',')  # 系列解包赋值
    order_ticket(row_num, row, column)
