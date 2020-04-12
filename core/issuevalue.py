# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 11:49
# @Author  : Ming Li
# @FileName: issuevalue.py
# @Software: PyCharm

# 1. Note that in this version, the number value is not continuous, transfer to [high, low, stepsize] format.
# Might have bug when the value size is too big.
# 2. json deserialize and serialize function are not implement yet.

import re
from typing import Any, Callable, Dict, List, Optional, Set, Union

class Value:
    pass

class ValueSet:

    def __init__(self):
        pass


class DiscreteValue(Value):
    pass

class DiscreteValueSet(ValueSet):
    pass

class NumberValue(Value):
    pass

class NumeberValueSet(ValueSet):
    pass

class Domain:

    def __init__(self, domainName: str, issueValueSet):
        if domainName == None:
            raise ValueError("Domain name is none!")

        if not re.match('[a-zA-Z0-9]+', domainName):
            raise ValueError(
                'domain name can have only simple characters but found ' + domainName)

        if issueValueSet == None:
            raise ValueError('issues is none!')

        for issue in issueValueSet:
            if issueValueSet[issue] == None:
                raise ValueError('valueset of '+ issue + ' is Empty!')
            if not isinstance(issueValueSet, ValueSet):
                raise TypeError('require a ValueSet!')

        self.name = domainName
        self.issueValueSet = issueValueSet

    def toString(self):
        return 'Domain[' + self.name + ',' + self.issueValueSet + ']'

    @property
    def getName(self):
        return self.name

    @property
    def getIssues(self):
        return list(self.issueValueSet)

    @property
    def getValueSet(self, issue: str): #可以加一个判断
        return self.issueValueSet[issue]

    def isComplete(self, bid):
        if not isinstance(bid, Bid):
            raise TypeError('input should be a Bid!')

        if list(self.issueValueSet) != bid.getIssues():
            return 'Issues in bid (' + bid.getIssues() \
                   + ') do not match issues in domain (' + list(self.issueValueSet) + ')'

        for issue in list(self.issueValueSet):
            if bid.getValue(issue) not in self.issueValueSet[issue]:
                return 'bid issue ' + issue + 'has illegal value' + bid.getValue(issue)

        return True

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass



class Bid:

    def __init__(self, issuevalues: dict):

        if (issuevalues == None):
            raise ValueError('issuevalues is none!')

        for issue in issuevalues.keys():
            if (issuevalues[issue] == None):
                raise ValueError('value of issue: '+ issue + ' can not be none!')

        self.issuevalue = issuevalues

    @property
    def getIssues(self):
        return list(self.issuevalue)

    @property
    def getIssueNum(self):
        return len(self.issuevalue)

    def contianIssue(self, issue: str):
        '''
        description
        :param issue:
        :return:
        '''
        return issue in self.issuevalue

    def getValue(self, issue: str):
        return self.issuevalue[issue]

    def update(self):
        pass

    def toString(self):
        pass

    def __hash__(self):
        pass  #hascode is to verify the unique of a bid.

    # partial bid not defined yet.
    def __eq__(self, other):
        pass

    # def equals(self, bid):
    #     if isinstance(bid, Bid):
    #         return self.issuevalue == bid.issuevalue
    #     else:
    #         raise TypeError('input is not a bid!')

def loadDomain(domainfile):
    pass