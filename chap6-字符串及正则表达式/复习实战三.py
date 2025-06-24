lst = [
    ['编号', '名称', '品牌', '单价'],
    ['01', '电风扇', '美的', 500],
    ['02', '洗衣机', 'TCL', 1000],
    ['03', '微波炉', '老板', 400],
]

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i == 0:
            print(lst[i][j], end='\t\t\t\t')
        else:
            if j == 0:
                print("{0:0>6}".format(lst[i][j]), end='\t\t\t')
            elif j == 3:
                print("¥{0:.2f}".format(lst[i][j]), end='\t\t\t')
            else:
                print(lst[i][j], end='\t\t\t')
    print()
