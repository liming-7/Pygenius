# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 10:59
# @Author  : Ming Li
# @FileName: action.py
# @Software: PyCharm

# deine the actions agent can take. Comparison action is not supported yet.

import re
from core.domainbid import Bid

# note that the action name and bid can't be changed. use protected or private?

class Action:

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('input name should be string but got ' + str(type(name)))
        if not re.match('[a-zA-Z]\\w*', name):
            raise ValueError('name ' + name +
                             ' is not a letter followed by zero or more word characters (letter, digit or _)')
        self.actor = name  # actor 是谁做出了这个

    def getActor(self):
        return self.actor


class Offer(Action):

    def __init__(self, name, bid):
        super().__init__(name)
        if not isinstance(bid, Bid):
            raise TypeError('input bid should be Bid but got ' + str(type(name)))
        self.__bid = Bid

    @property #property的用法是不是有问题。。。。。
    def getBid(self):
        return self.__bid

    @property
    def toString(self):
        return 'Offer[ Actor: ' + self.getActor() + ', ' + self.__bid.toString() ##这里return的是Bid类型还是tostring后的


class Accept(Action):

    def __init__(self, name, bid):
        super().__init__(name)
        if not isinstance(bid, Bid):
            raise TypeError('input bid should be Bid but got ' + str(type(name)))
        self.__bid = bid

    @property
    def getBid(self):
        return self.__bid

    @property
    def toString(self):
        return 'Accept[ Actor: ' + self.getActor() + ', ' + self.__bid.toString() + ']'##这里return的是Bid类型还是tostring后的


class EndNegotiation(Action):

    def __init__(self, name):
        super().__init__(name)

    @property
    def toString(self):
        return 'EndNegoiation[ Actor: ' + self.getActor() + ']' ##这里return的是Bid类型还是tostring后的



class Silent(Action):

    def __init__(self, name):
        super().__init__(name)

    @property
    def toString(self):
        return 'Silent[ Actor: ' + self.getActor() + ']' ##这里return的是Bid类型还是tostring后的


class Comparison(Action):

    def __init__(self, name):
        super().__init__(name)


class ElicitComparison(Action):

    def __init__(self, name):
        super().__init__(name)
