# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : t.py
@Author  : Yebax
@Time    : 2018/12/19 21:21
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"
import re
f = open("02第二模块之三体语录.txt", 'r', encoding='utf-8')
r = f.readlines()
line = r[2]
new_line = line.replace('不要回答', '绝对不能回复')
print(new_line)
r[2] = new_line
# del r[-1]
r.insert(4, '给岁月以文明，而不是给文明以岁月\n')
r[-1] = '给时光以生命，而不是给生命以时光\n'
print(r[-1])
# for lines in r:
#     print(lines)
# print(r)

# for line in r:
#     print(line)
#     break
