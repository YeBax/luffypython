# -*- coding: utf-8 -*-
from multiprocessing import Process
import time


# 方法一
# def task(name):
#     print("%s is running..." % name)
#     time.sleep(3)
#     print("%s is done..." % name)
#
# if __name__ == '__main__':
#     p1 = Process(target=task, kwargs={"name":"子进程1"})
#     p2 = Process(target=task, args=('子进程2',))
#     p1.start()
#     p2.start()


# 方法二
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("%s is running..." % self.name )
        time.sleep(2)
        print("%s is done..." % self.name )

if __name__ == '__main__':
    p = MyProcess("process1")
    p.start()
