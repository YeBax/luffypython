# -*- coding: utf-8 -*-
from multiprocessing import Process
import time


def task(name):
    print("%s is running..." % name)
    time.sleep(2)

if __name__ == '__main__':
    p =Process(target=task, args=("子进程1",))
    p.daemon = True
    p.start()
    print("主")


