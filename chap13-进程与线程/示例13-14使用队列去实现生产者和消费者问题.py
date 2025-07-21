from queue import Queue
import time
from threading import Thread


# 创建一个生产者
class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 6):
            print(f'{self.name}将产品{i}放入队列')
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的存放')


# 创建一个消费者
class Consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for _ in range(5):
            value = self.queue.get()
            print(f'消费者线程:{self.name}取出了{value}')
            time.sleep(1)
        print('消费者线程完成了所有数据的取出')


if __name__ == '__main__':
    queue = Queue()
    producer = Producer('生产者', queue)
    consumer = Consumer('消费者', queue)
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('主线程执行完毕')