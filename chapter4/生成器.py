# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : 生成器.py
@Author  : Yebax
@Time    : 2018/12/19 22:10
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"
li = [1, 2, 3, 5, 5, 6, 7, 8, 9, 9, 8, 3]
l = [x * 2 for x in li]
# print(l)
# for x in l:
#     print(x)

# if type('s') is str:
#     print(1)
# if isinstance('s',str):
#     print(2)

from functools import reduce
a = reduce(lambda x,y:x+y,range(10))
print(a)