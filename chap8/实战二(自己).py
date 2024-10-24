def get_digit(param):
    s = 0
    lst = []
    for item in param:
        if item.isdigit():
            lst.append(int(item))
    s = sum(lst)
    return s, lst


ins = input('请输入一个字符串')
total, elements = get_digit(ins)
print(total)
print(elements)
