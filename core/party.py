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
        self.check_complement()

    def choose_action(self):
        pass

    def check_complement(self): #查找是否有chooseAction这个函数，或者一些其他函数。
        pass


class UtilitySpace:
    pass


class Party:
    '''
    the basic party
    '''

    def __init__(self, name, capabilities: protocol_Set, strategy = None, utility_space = None):
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
        self.utility_space = utility_space

    def set_strategy(self, strategy):
        self.strategy = strategy

    def set_utility_space(self, utility_space):
        self.utility_space = utility_space

    def set_description(self, des: str):
        self.description = des

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def get_capabilities(self):
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
