#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 1:49
# @Author  : Ziang Qiu
# @contact : z.qiu@student.tudelft.nl
# @File    : BidIterator.py
from functools import reduce


def create_bid_iterator(domain):
    bid_list = []
    issue_value_list = []
    issue_value = domain.get_issue_values()
    issue_name, issue_list = generate_issue_value_list(issue_value)
    all_bid_list = lists_combination(issue_value, "丨")
    for index in all_bid_list:
        temp_list = index.split("丨")
        temp = {}
        for issues in range(len(issue_name)):
            temp[issue_name[issues]] = temp_list[issues]
        bid_list.append({"issuevalues": temp})
    return bid_list


def generate_issue_value_list(issues):
    result_list = []
    name_list = []
    for index in issues.keys():
        temp_value = index[index]["value"]
        result_list.append(temp_value)
        name_list.append(index)
    return name_list, result_list


def lists_combination(lists, code):
    def merge(list1, list2):
        return [str(i) + code + str(j) for i in list1 for j in list2]

    return reduce(merge, lists)
