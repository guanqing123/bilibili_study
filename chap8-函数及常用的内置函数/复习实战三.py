x = input('请输入')
print(x)

def u2U2u(x):
    lst = []
    for i in x:
        if i.islower():
            lst.append(i.upper())
        elif i.isupper():
            lst.append(i.lower())
        else:
            lst.append(i)
    return lst

lst = u2U2u(x)
# list转字符串
str = ''.join(lst)
print(str)
