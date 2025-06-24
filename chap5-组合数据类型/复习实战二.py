lst = []
for i in range(5):
    good = tuple(input('请输入产品代码和名称,用空格隔开').split(' '))
    lst.append(good)
print(lst)

cart = []
flag = True
while flag:
    goodId = input('请输入产品代码:')
    if goodId == 'q':
        flag = False
    else:
        for item in lst:
            if goodId == item[0]:
                cart.append(item)
                break  # 跳出for循环
        else:
            print('没有此商品' + goodId)
else:
    #     逆序显示cart
    for item in reversed(cart):
        print(item)
