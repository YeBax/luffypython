# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : 装饰.py
@Author  : Yebax
@Time    : 2018/12/19 21:57
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"

user = {
    'username':'abc',
    'password' : '123456',
    'state': True
}


def check_login(func):
    def inner(*args, **kwargs):
        if args[0]['state'] == True:
            return func(*args, **kwargs)
        else:
            print('未登录！')
    return inner


@check_login
def login(user):
    print('1')

if __name__ == '__main__':
    login(user)