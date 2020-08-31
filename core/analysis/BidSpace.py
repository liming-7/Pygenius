#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 16:48
# @Author  : Ziang Qiu
# @contact : z.qiu@student.tudelft.nl
# @File    : BidSpace.py
import Global
import BidIterator
import BidPoint


class BidSpace:
    def __init__(self, utility_space_a, utility_space_b):
        self.space_a = utility_space_a
        self.space_b = utility_space_b
        self.bid_points = []
        if utility_space_a is None or utility_space_b is None:
            raise Exception("util space is empty")
        self.domain = self._space_a.get_domain()
        self.space_a.check_ready_for_negotiation("space_a", self.domain)
        self.space_b.check_ready_for_negotiation("space_b", self.domain)
        self.pareto_frontier = None
        self.kalai_smorodinsky = None
        self.nash = None
        if Global.low_memory_mode:
            self.build_space(True)
        else:
            self.build_space(False)

    def build_space(self, exclude_bids):
        bid_iterator = BidIterator.create_bid_iterator(self.domain)
        if exclude_bids:
            for index in bid_iterator:
                self.bid_points.append(
                    BidPoint.BidPoint(None, self.space_a.get_utility(index), self.space_b.get_utility(index)))
        else:
            for index in bid_iterator:
                self.bid_points.append(
                    BidPoint.BidPoint(index, self.space_a.get_utility(index), self.space_b.get_utility(index)))

    def get_pareto_frontier(self):
        is_bid_space_available = len(self.bid_points) != 0
        if self.pareto_frontier is None:
            if is_bid_space_available:
                pass

    def compute_pareto_frontier(self, points):
        pass
