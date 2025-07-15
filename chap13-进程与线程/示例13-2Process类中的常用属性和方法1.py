import os
import time
from multiprocessing import Process


# 函数式方式创建子进程
def sub_process(name):
    print('子进程%s（%s）启动, 父进程的pid是%s' % (name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('子进程%s结束' % name)


def sub_process2(name):
    print(f'子进程{name}（{os.getpid()}）启动, 父进程的pid是{os.getppid()}')
    time.sleep(1)
    print(f'子进程{name}结束')


if __name__ == '__main__':
    # 主进程
    print(f'主进程启动, pid是{os.getpid()}')
    for i in range(5):
        # 创建第一个子进程
        p1 = Process(target=sub_process, args=('boy' + str(i),))
        # 创建第二个子进程
        p2 = Process(target=sub_process2, args=('girl' + str(i),))
        # 调用start()启动子进程
        p1.start()
        p2.start()
        print(p1.name, '是否执行完毕:', p1.is_alive())
        print(p2.name, '是否执行完毕:', p2.is_alive())

        print(p1.name, 'pid是：', p1.pid)
        print(p2.name, 'pid是：', p2.pid)

        p1.join()  # 主进程要等待p1执行结束, 阻塞主进程
        p2.join()  # 主进程要等待p2执行结束

        print(p1.name, '是否执行完毕:', p1.is_alive())
        print(p2.name, '是否执行完毕:', p2.is_alive())

    print('父进程执行完毕')
