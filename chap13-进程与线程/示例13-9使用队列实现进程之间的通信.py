import time
from multiprocessing import Queue, Process

a = 100


def write_msg(q):
    global a
    if not q.full():
        for i in range(6):
            a -= 10
            q.put(a)  # 入队
            print('a入队的值:', a)


def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('a出队列的值:', q.get())


if __name__ == '__main__':
    print('主进程启动')
    q = Queue()  # 由父进程创建的队列,没有指定参数,说明可接收消息的个数没有上限
    p1 = Process(target=write_msg, args=(q,))
    p2 = Process(target=read_msg, args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('主进程结束')
