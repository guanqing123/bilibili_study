import threading
import time
from threading import Thread


def test():
    for i in range(3):
        time.sleep(1)
        print(f'线程{threading.current_thread().name}正在运行{i}')


if __name__ == '__main__':
    start = time.time()
    print('主线程开始执行')

    lst = [Thread(target=test) for i in range(2)]

    for item in lst:
        item.start()

    for item in lst:
        item.join()

    print(f'主线程结束执行,耗时{time.time()-start}')
