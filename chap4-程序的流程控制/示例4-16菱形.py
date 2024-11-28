row = eval(input('请输入菱形的行数：'))
while row % 2 == 0:  # 判断行数的奇偶性,行数是偶数,重新输入行数
    row = eval(input('请输入菱形的行数：'))

top_row = (row + 1) // 2
for i in range(1, top_row + 1):
    for k in range(1, top_row + 1 - i):
        print(' ', end='')
    for j in range(1, 2 * i):
        print('*', end='')
    print('')

bottom_row = (row - 1) // 2
for i in range(1, bottom_row + 1):
    # 直角三角形
    for j in range(1, i+1):
        print(' ', end='')

    # 倒三角
    for k in range(1, 2 * bottom_row - 2*i + 2):
        print('*', end='')
    print()
