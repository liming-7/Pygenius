# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 11:52
# @Author  : Ming Li
# @FileName: party.py
# @Software: PyCharm

#要考虑到不同名字的agent可能会用一种strategy， 并且在进行过程中方便随时更换新的strategy，
# 同时需要考虑strategy可以在negotiation中可以更新， 因而对strategy与agent进行分离。

import re
from typing import Any, Callable, Dict, List, Optional, Set, Union

from core.action import *

protocol_Set = Set[str]


class Strategy:
    # All strategy should have this
    def __init__(self):
        self.checkComplement()

    def chooseAction(self):
        pass

    def checkComplement(self): #查找是否有chooseAction这个函数，或者一些其他函数。
        pass


class UtilitySpace:
    pass


class Party:
    '''
    the basic party
    '''

    def __init__(self, name, capabilities: protocol_Set, strategy = None, utilityspace = None):
        if not isinstance(name, str):
            raise TypeError('input name should be string but got ' + str(type(name)))
        if not re.match('[a-zA-Z]\\w*', name):
            raise ValueError('name ' + name +
                             ' is not a letter followed by zero or more word characters (letter, digit or _)')
        if capabilities is None:
            raise ValueError('suppoeted protocol is None!')

        self.name = name
        self.supprotocol = capabilities
        self.strategy = strategy
        self.utilitySpace = utilityspace

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

    def serialize(self):
        pass

    def deserialize(self):
        pass
