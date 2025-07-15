from multiprocessing import Process

a = 100


def add():
    global a
    print('子进程1开始执行,a=', a)
    a += 30
    print('子进程1结束,a=', a)


def sub():
    global a
    print('子进程2开始执行,a=', a)
    a -= 50
    print('子进程2结束, a=', a)


if __name__ == '__main__':
    print('父进程开始执行, a=', a)
    p1 = Process(target=add)
    p2 = Process(target=sub)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('父进程结束, a=', a)
