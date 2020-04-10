# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 11:52
# @Author  : Ming Li
# @FileName: party.py
# @Software: PyCharm

import re
from typing import Any, Callable, Dict, List, Optional, Set, Union

protocol_Set = Set[str]

class Capabilities:

    def __init__(self, protocol: protocol_Set):
        '''

        :param protocol: Set of supported protocols.
        '''
        if protocol == None:
            raise ValueError('suppoeted protocol is None!')
        self.supportProtocol = protocol

    def getSupportProtocol(self) -> protocol_Set:
        return self.supportProtocol

    def hasCode(self):
        pass

    def equals(self):
        pass

class Party:
    '''
    the basic party
    '''
    def __init__(self):
        pass

class SimulateParty(Party):
    '''
    use in algorithm simulation
    '''
    pass

class WebParty(Party):
    '''
    use in real negotiation nodes via Web service
    '''
    pass