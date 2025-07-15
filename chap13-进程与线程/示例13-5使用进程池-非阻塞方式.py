import os
import time
from multiprocessing import Pool


def task(name):
    print(f'子进程{name}（{os.getpid()}）启动, 父进程的pid是{os.getppid()}')
    time.sleep(1)


if __name__ == '__main__':
    # 主进程
    start = time.time()
    print(f'父进程{os.getpid()}开始启动')
    # 创建进程池
    pool = Pool(3)
    # 创建任务
    for i in range(10):
        # 以非阻塞的方式
        pool.apply_async(func=task, args=(i,))

    pool.close()  # 关闭进程池不再接受新的任务
    pool.join()  # 阻塞父进程
    print('所有的子进程执行完毕，父进程执行结束')
    print(f'父进程结束, 耗时{time.time() - start}')
