s = 0
for i in range(1, 101):
    if i % 2 == 1:
        continue
    else:
        s += i
else:
    print('1-100之间的偶数和', s)
