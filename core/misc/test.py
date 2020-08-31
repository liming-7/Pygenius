#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 19:24
# @Author  : Ziang Qiu
# @contact : z.qiu@student.tudelft.nl
# @File    : test.py

class Temp:
    def __init__(self):
        self.a = 10


if __name__ == '__main__':
    temp = Temp()
    print(temp.b is None)
