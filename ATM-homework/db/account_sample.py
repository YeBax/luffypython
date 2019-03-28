# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : account_sample.py
@Author  : Yebax
@Time    : 2018/12/17 0:39
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"

import json
acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

# print(json.dumps(acc_dic))