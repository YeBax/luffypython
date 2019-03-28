# -*- coding: utf-8 -*-
import json
import time
from multiprocessing import Process, Lock


def search(name):
    dic = json.load(open("db.txt", "r", encoding="utf-8"))
    print('<%s>查看剩余票数【%s】' % (name, dic["count"]))


def get(name):
    time.sleep(1)
    dic = json.load(open("db.txt", "r", encoding="utf-8"))
    if dic["count"] > 0:
        dic["count"] -= 1
        time.sleep(3)
        json.dump(dic, open("db.txt", "w", encoding="utf-8"))
        print('<%s>购票成功' % name)
    else:
        print("购票失败！")


def task(name):
    search(name)
    get(name)

if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = p =Process(target=task, args=(i, ))
        p.start()
        p.join()
