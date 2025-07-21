from threading import Thread

a = 100


def add():
    print('加线程开始执行')
    global a
    a += 30
    print(f'a的值为:{a}')
    print('加的线程执行结束')


def sub():
    print('减线程开始执行')
    global a
    a -= 50
    print(f'a的值为:{a}')
    print('减的线程执行结束')


if __name__ == '__main__':
    print('主线程开始执行')
    print(f'全部变量a的值: {a}')

    t1 = Thread(target=add)
    t2 = Thread(target=sub)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f'a的值为:{a}')
