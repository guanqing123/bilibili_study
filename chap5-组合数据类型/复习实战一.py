lst = [88, 89, 90, 98, 0, 99]
print(lst)
# for i in range(len(lst)):
#     if lst[i] == 0:
#         lst[i] = '200' + str(lst[i])
#     else:
#         lst[i] = '19' + str(lst[i])
#
# print(lst)

newlst = []
for item in lst:
    if item == 0:
        item = '200' + str(item)
    else:
        item = '19' + str(item)
    newlst.append(item)
print(newlst)