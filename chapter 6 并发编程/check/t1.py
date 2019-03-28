# -*- coding: utf-8 -*-
import time
from queue import Queue
from threading import Thread


def producer(q):
    # 生产者
    num = 1
    while True:
        s = "生产者,第%s产品" % num
        print("已经生产：",s)
        num += 1
        q.put(s)
        time.sleep(3)


def consumer(q):
    # 消费者
    while True:
        s = q.get()
        print("消费：%s" % s)
        time.sleep(1)


if __name__ == '__main__':
    q = Queue()
    p1 = Thread(target=producer, args=(q,))
    p2 = Thread(target=producer, args=(q,))
    p3 = Thread(target=producer, args=(q,))
    c1 = Thread(target=consumer, args=(q,))
    c2 = Thread(target=consumer, args=(q,))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    c1.join()
    c2.join()
