# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : atm.py
@Author  : Yebax
@Time    : 2018/12/16 23:15
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"


import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(base_dir)
sys.path.append(base_dir)

from core import main

if __name__ == '__main__':
    main.run()