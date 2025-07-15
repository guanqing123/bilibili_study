import os
import time
from multiprocessing import Process


# 自定义一个类
class SubProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('子进程%s（%s）启动, 父进程pid为:%s' % (self.name, self.pid, os.getppid()))
        time.sleep(1)


if __name__ == '__main__':
    print(f'父进程开始执行, pid 为 {os.getpid()}')

    lst = []
    for i in range(5):
        p = SubProcess(f'进程名:{i}')
        # 启动进程
        p.start()
        lst.append(p)

    # 阻塞一下主进程
    for thread in lst:
        thread.join()

    print(f'父进程结束')
