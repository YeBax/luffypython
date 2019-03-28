# -*- coding: utf-8 -*-
from multiprocessing import Queue

q = Queue(3)

q.put("hello")
q.put({"a":1})
q.put([1,2,3])
print(q.full())
# q.put(3)
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
print(q.get())