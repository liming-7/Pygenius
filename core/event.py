# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 11:00
# @Author  : Ming Li
# @FileName: event.py
# @Software: PyCharm

# deine the negotiation event. 主要为了实际negotiation节点的event。Protocol负责记录下来。
import datetime
from core.action import *

class Event:

    def __init__(self):
        self._time = datetime.time

    def getTime(self):
        return self._time

class ActionEvent(Event):

    def __init__(self, action):
        super().__init__()
        if not isinstance(action, Action):
            raise TypeError('input name should be an Action but got ' + str(type(action)))
        self.__action = action

    def getAction(self):
        return self.__action

    def toString(self):
        return type(self).__name__ + '[' + str(self.getTime()) + ',' + self.getAction().toString() + ']'