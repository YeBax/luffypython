# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : 日志.py
@Author  : Yebax
@Time    : 2018/12/19 22:21
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"

import logging
from logging import handlers

# logger = logging.FileHandler('example.log', encoding='utf-8')
fh = logging.FileHandler('example.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d', datefmt='%m/%d/%Y %I:%M:%S %p')
fh.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
# handlers.TimedRotatingFileHandler()

logger.debug('debug')

