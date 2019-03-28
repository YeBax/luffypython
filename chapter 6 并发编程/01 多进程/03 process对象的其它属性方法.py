# -*- coding: utf-8 -*-


from multiprocessing import Process
import time, os

# def task(name):
#     print("%s is running... pid:%s" % (name, os.getpid()))
#     print("parent pid:%s" % os.getppid())
#     time.sleep(3)
#     print("%s is done... pid:%s" % (name, os.getpid()))
#
# if __name__ == '__main__':
#     p1 = Process(target=task, kwargs={"name": "子进程1"})
#     p1.start()
#
#     p1.join()
#     print("主pid:",os.getpid(), os.getppid())


def task(name, n):
    print("%s is running... pid:%s" % (name, os.getpid()))
    print("parent pid:%s" % os.getppid())
    time.sleep(n)
    print("%s is done... pid:%s" % (name, os.getpid()))


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=("子进程1", 5))
    p2 = Process(target=task, args=("子进程2", 6), name="haha")
    p3 = Process(target=task, args=("子进程3", 2))
    p1.start()
    print(p1.terminate())
    p2.start()
    p3.start()
    print(p2.name)

    p1.join()
    p2.join()
    p3.join()

    print("主pid:", os.getpid(), os.getppid())
    print(time.time()-start)
    print(p1.is_alive())
    print(p1.terminate())

