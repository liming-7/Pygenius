#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 17:11
# @Author  : Ziang Qiu
# @contact : z.qiu@student.tudelft.nl
# @File    : BidPoint.py
import math


class BidPoint:
    def __init__(self, bid, utility_a, utility_b):
        self.bid = bid
        self.utility_a = utility_a
        self.utility_b = utility_b

    def distance_to(self, point):
        return math.sqrt(math.pow(self.utility_a - point.utility_a, 2) + math.pow(self.utility_b - point.utility_b, 2))

    def is_dominated_by(self, point):
        if self != point:
            if point.utility_a >= self.utility_a and point.utility_b >= self.utility_b:
                return True
        return False