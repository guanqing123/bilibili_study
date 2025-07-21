from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)
    # 向队列中添加元素(入队)
    q.put('hello')  # block=True
    q.put('world')
    q.put('Python')

    # raise Full
    # queue.Full 等待2秒之后,队列还没有空位置,则抛出异常
    q.put('html', block=True, timeout=2)
