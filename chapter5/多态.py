# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffypython
@File    : 多态.py
@Author  : Yebax
@Time    : 2019/1/4 0:56
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"

import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def talk(self):
        pass

class People(Animal):
    def talk(self):
        print("say hello")
 
p = People()
p.talk()

