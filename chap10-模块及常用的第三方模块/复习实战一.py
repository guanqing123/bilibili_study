# for i in range(0, 7):
#     for j in range(0, 6):
#         if i == 0 and j == 0:
#             print('行号', end='\t')
#         elif i == 0:
#             print(f'座位{j}', end='\t')
#         elif j == 0:
#             print(f'第{i}行', end='\t')
#         else:
#             print('有票', end='\t')
#     print()

from prettytable import PrettyTable


def show_ticket(row_num, col_num):
    tb = PrettyTable()
    header = []
    for i in range(0, col_num + 1):
        if i == 0:
            header.append('行号')
        else:
            header.append(f'座位{i}')
    tb.field_names = header
    for j in range(1, row_num + 1):
        lst = [f'第{j}行']
        for k in range(1, col_num + 1):
            lst.append('有票')
        tb.add_row(lst)
    return tb


def order_ticket(row_num, col_num, row, col):
    tb = PrettyTable()
    header = []
    for i in range(0, col_num + 1):
        if i == 0:
            header.append('行号')
        else:
            header.append(f'座位{i}')
    tb.field_names = header
    for j in range(1, row_num + 1):
        lst = [f'第{j}行']
        for k in range(1, col_num + 1):
            if int(row) == j and int(col) == k:
                lst.append('已售')
            else:
                lst.append('有票')
        tb.add_row(lst)
    return tb


beg = show_ticket(6, 5)
print(beg)
inp = input('请输入您的座位:(如4,3)')
row, col = inp.split(',')
end = order_ticket(6, 5, row, col)
print(end)
