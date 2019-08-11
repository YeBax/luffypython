# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : main.py
@Author  : Yebax
@Time    : 2019/8/10 19:07
-----------------------------------
    ==Oh Captain! My Captain!==
"""
from wsgiref.simple_server import make_server
from urls import *
__author__ = "Yebax"


def application(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html')])
    print('PATH', environ.get('PATH_INFO'))

    # 当前请求路径
    path = environ.get('PATH_INFO')

    # if path == "/favicon.ico":
    #     with open("favicon.ico", "rb") as f:
    #         data = f.read()
    #         return [data]
    # elif path == "/login":
    #     with open("login.html", "rb") as f:
    #         data = f.read()
    #         return [data]
    #
    # elif path == "/index":
    #     with open("index.html", "rb") as f:
    #         data = f.read()
    #         return [data]

    func = None
    for item in url_patterns:
        if path == item[0]:
            func = item[1]
            break

    if func:
        return [func()]
    else:
        return [b'404!']

# 封装socket
httped = make_server("", 8080, application)

# 等待用户连接: conn, addr=sock.accept()
httped.serve_forever()      # application(environ, start_response)
