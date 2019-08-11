# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : urls.py
@Author  : Yebax
@Time    : 2019/8/10 20:10
-----------------------------------
    ==Oh Captain! My Captain!==
"""
from view import *
__author__ = "Yebax"


url_patterns = [
        ("/login", login),
        ("/index", index),
        ("/favicon.ico", favicon),
        ("/reg", reg),
        ("/timer", timer),
    ]