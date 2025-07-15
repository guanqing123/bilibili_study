import os
from multiprocessing import Process


# 函数式方式创建子进程
def sub_process1(name):
    print('子进程%s（%s）启动, 父进程pid是: %s' % (name, os.getpid(), os.getppid()))


def sub_process2(name):
    print('子进程%s（%s）启动, 父进程pid是: %s' % (name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    # 主进程
    print(f'主进程开始执行')
    for i in range(5):
        # 创建第一个子进程
        # p1 = Process()  # 没有给定target参数,不会执行自己编写的函数中的代码,会调用执行Process类中的run方法
        # # 创建第二个子进程
        # p2 = Process()
        # p1.start()  # 调用Process类中的run方法执行
        # p2.start()
        # p1.join()
        # p2.join()

        p3 = Process(target=sub_process1, args=('boy' + str(i),))
        p4 = Process(target=sub_process2, args=('girl' + str(i),))
        p3.start()  # 如果Process类创建对象时指定了target参数,start()调用target指定的函数去执行
        p4.start()

        # p3.join()
        # p4.join()

        # 终止进程
        p3.terminate()
        p4.terminate()

    print(f'主进程执行结束')
