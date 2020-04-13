# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 11:52
# @Author  : Ming Li
# @FileName: party.py
# @Software: PyCharm

import re
from typing import Any, Callable, Dict, List, Optional, Set, Union

from core.action import *

protocol_Set = Set[str]


class Strategy:
    pass


class UtilitySpace:
    pass


class Party:
    '''
    the basic party
    '''

    def __init__(self, name, capabilities: protocol_Set):
        if not isinstance(name, str):
            raise TypeError('input name should be string but got ' + str(type(name)))
        if not re.match('[a-zA-Z]\\w*', name):
            raise ValueError('name ' + name +
                             ' is not a letter followed by zero or more word characters (letter, digit or _)')
        if capabilities is None:
            raise ValueError('suppoeted protocol is None!')


        self.name = name
        self.supprotocol = capabilities

    def setStrategy(self, strategy):
        self.strategy = strategy

    def setUtilitySpace(self, utilityspace):
        self.utilitySpace = utilityspace

    def setDescription(self, des: str):
        self.description = des

    def getDescription(self):
        return self.description

    def getName(self):
        return self.name

    def getCapabilities(self):
        return self.supprotocol


class SimulateParty(Party):
    '''
    use in algorithm simulation
    '''

    def __init__(self, name, capabilities):
        super().__init__(name, capabilities)


class WebParty(Party):
    '''
    use in real negotiation nodes via Web service
    '''
    def __init__(self, name, capabilities):
        super().__init__(name, capabilities)

    def seril
