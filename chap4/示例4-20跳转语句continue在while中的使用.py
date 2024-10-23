i = 0
s = 0
while i <= 100:
    if i % 2 == 1:
        i += 1
        continue
    else:
        s += i
        i += 1
else:
    print("1-100之间的偶数和", s)
