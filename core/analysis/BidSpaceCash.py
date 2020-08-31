#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 18:47
# @Author  : Ziang Qiu
# @contact : z.qiu@student.tudelft.nl
# @File    : BidSpaceCash.py

bid_space_cash = {}


def add_bid_space_to_cash(utility_space_a, utility_space_b, bid_space):
    if utility_space_a in bid_space_cash:
        if utility_space_b in bid_space_cash[utility_space_a]:
            bid_space_cash[utility_space_a][utility_space_b] = bid_space
    else:
        cash_a = {utility_space_b: bid_space}
        bid_space_cash[utility_space_a] = cash_a


def get_bid_space(utility_space_a, utility_space_b):
    if utility_space_a in bid_space_cash:
        return bid_space_cash[utility_space_a][utility_space_b]
    else:
        return None


def remove_bid_space(utility_space_a, utility_space_b):
    # if this dict is empty, it returns false, else it returns true.
    empty = bool(bid_space_cash)
    if not empty:
        if utility_space_a in bid_space_cash:
            if utility_space_b in bid_space_cash[utility_space_a]:
                del bid_space_cash[utility_space_a][utility_space_b]
            if len(bid_space_cash[utility_space_a]) == 0:
                del bid_space_cash[utility_space_a]


def get_domains_count():
    return len(bid_space_cash)
