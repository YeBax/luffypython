# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import time


def producer(q, name):
    for i in range(10):
        res = "%s的包子%s" % (name, i)
        time.sleep(0.5)
        print("生产者%s,生产了%s" % (name, res))

        q.put(res)


def consumer(q):
    while True:
        res = q.get()
        if res is None:break
        time.sleep(1)
        print("消费者吃了%s" % res)

if __name__ == '__main__':
    # 容器
    q = Queue()

    # 生产者
    p1 = Process(target=producer, args=(q, "A"))
    p2 = Process(target=producer, args=(q, "B"))
    p3 = Process(target=producer, args=(q, "C"))
    p4 = Process(target=producer, args=(q, "D"))
    p5 = Process(target=producer, args=(q, "E"))
    p = [p1, p2, p3, p4, p5]

    # 消费者
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c3 = Process(target=consumer, args=(q,))
    c = [c1, c2, c3]

    for _ in p:
        _.start()
        _.daemon = True

    for _ in c:
        _.start()

    for _ in p:
        _.join()
        q.put(None)
    for _ in c:
        _.join()
    print("主 main")
