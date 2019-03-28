# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : log_test.py
@Author  : Yebax
@Time    : 2018/12/12 1:05
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"

import logging
from logging import handlers

class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record):  # 固定写法
        return "db backup" not in record.getMessage()

logger = logging.getLogger("web")
logger.setLevel(logging.DEBUG)
logger.addFilter(IgnoreBackupLogFilter())

ch = logging.StreamHandler()
# fh = logging.FileHandler("web.log")
# fh = handlers.RotatingFileHandler("web.log", maxBytes=500, backupCount=3)
fh = handlers.TimedRotatingFileHandler("timelog.log", when="s", interval=5,backupCount=5)


# ch.setLevel(logging.INFO)
fh.setLevel(logging.ERROR)

logger.addHandler(ch)
logger.addHandler(fh)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')

fh.setFormatter(file_formatter)
ch.setFormatter(console_formatter)


logger.debug("debug test log")
logger.info("info test log")
logger.error("error test log")
logger.warning("warning test log")
logger.debug("-------------------------")
logger.debug("-------db backup-------")
logger.debug("-------db1 backup-------")
logger.debug("-------db2 backup-------")