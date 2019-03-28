# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : 自定义元类.py
@Author  : Yebax
@Time    : 2019/1/13 0:06
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"


class Mymeate(type):
    def __init__(self, class_name, class_cases, class_dic):
        if not class_name.istitle():
            raise TypeError('首字母必须大写')
        super(Mymeate,self).__init__(class_name, class_cases, class_dic)

    def __call__(self, *args, **kwargs):
        pass


class Chinese(object, metaclass=Mymeate):
    county = 'China'
    def __init__(self, name, age):
        self.name =name
        self.age = age
    def __call__(self, *args, **kwargs):
        pass

