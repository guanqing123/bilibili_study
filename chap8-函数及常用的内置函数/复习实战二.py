z_in = input('请输入一个字符串')
print(z_in, type(z_in))
lst = list(z_in)


def get_list_sum(lst):
    s = 0
    tplst = []
    for i in lst:
        if i.isdigit():
            tplst.append(int(i))
            s += int(i)
    return s, tplst


total, lst = get_list_sum(lst)
print(f'提取的数字列表为: {lst}')
print(f'累加和为: {total}')
