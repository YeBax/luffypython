# -*- coding: utf-8 -*-
import os
import sys
from selection.courseSystem import login, Manager, Student, Teacher

ret = login()
if ret["result"]:
    print("登录成功")
    if hasattr(sys.modules[__name__], ret['id']):
        cls = getattr(sys.modules[__name__], ret['id'])
        obj = cls.init(ret['name'])
        while True:
            for id, item in enumerate(cls.operate_lst, 1):
                print(id, item[0])
            func_str = cls.operate_lst[int(input(">>>"))-1][1]
            if hasattr(obj, func_str):
                getattr(obj, func_str)()
else:
    print("登录失败")
