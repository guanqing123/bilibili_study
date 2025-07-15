import os
import time
from multiprocessing import Process


def thread():
    print(f'我是子进程,我的pid是{os.getpid()}, 父进程的pid是{os.getppid()}')
    time.sleep(1)


if __name__ == '__main__':
    print(f'我是主进程,我的pid是{os.getpid()}')
    lst = []
    # 创建5个子进程
    for i in range(5):
        # 创建子进程
        p = Process(target=thread)
        # 启动子进程
        p.start()
        # 启动中的子进程加入列表
        lst.append(p)

    # 遍历lst,列表中五个子进程
    for e in lst:   # e的数据类型是 Process类型
        e.join()    # 阻塞主进程

    print(f'主进程结束')
