import random

rand = random.randint(0, 100)  # 产生1-100之间的随机数
count = 1  # 记录猜数的次数
while count <= 10:
    guess = eval(input('在我心中有个数,1-100之间,请您猜一猜'))
    if guess == rand:
        print('数字为', guess, '恭喜您猜中了!花费了', count, '次机会')
    elif guess > rand:
        print('猜大了')
    elif guess < rand:
        print('猜小了')
    count += 1
else:
    print('10次都没猜中')
