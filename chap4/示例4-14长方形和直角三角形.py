# 三行四列
for i in range(1, 4):  # 外层循环 行
    for j in range(1, 5):  # 内层循环 列
        print('*', end='')
    print()  # 空的print语句,作用是换行
print('-' * 20)

# 直角三角形
for i in range(1, 6):
    for j in range(0, i):
        print('*', end='')
    print()

print('-'*20)
