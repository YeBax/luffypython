# -*- coding: utf-8 -*-
import json
import time
from multiprocessing import Process, Lock


def search(name):
    dic = json.load(open("db.txt", "r", encoding="utf-8"))
    print('<%s>查看剩余票数【%s】' % (name, dic["count"]))


def get(name, mutex):
    mutex.acquire()
    time.sleep(1)
    dic = json.load(open("db.txt", "r", encoding="utf-8"))
    if dic["count"] > 0:
        dic["count"] -= 1
        time.sleep(3)
        json.dump(dic, open("db.txt", "w", encoding="utf-8"))
        print('<%s>购票成功' % name)
    mutex.release()


def task(name, mutex):
    search(name)
    # mutex.acquire()
    get(name, mutex)
    # mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = p =Process(target=task, args=(i, mutex))
        p.start()
