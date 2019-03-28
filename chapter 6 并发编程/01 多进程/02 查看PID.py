# -*- coding: utf-8 -*-
from multiprocessing import Process
import time, os


def task(name):
    print("%s is running... pid:%s" % (name, os.getpid()))
    print("parent pid:%s" % os.getppid())
    time.sleep(3)
    print("%s is done... pid:%s" % (name, os.getpid()))

if __name__ == '__main__':
    p1 = Process(target=task, kwargs={"name": "子进程1"})
    p1.start()

    print("主pid:",os.getpid())


