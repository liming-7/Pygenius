# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 11:49
# @Author  : Ming Li
# @FileName: issuevalue.py
# @Software: PyCharm

from typing import Any, Callable, Dict, List, Optional, Set, Union

class Domain:

    def __init__(self, domainName: str, issueValueSet: dict):
        if domainName == None:
            raise ValueError("Domain name is none!")

        if issueValueSet == None:
            raise ValueError('issues is none!')

        for issue in issueValueSet:
            if issueValueSet[issue] == None:
                raise ValueError('valueset of '+ issue + ' is Empty!')

        self.name = domainName
        self.issueValueSet = issueValueSet

    def getName(self):
        return self.name

    def getIssues(self):
        return list(self.issueValueSet)


class Issue:
    pass

class Bid:

    def __init__(self, issuevalues: dict):

        if (issuevalues == None):
            raise ValueError('issuevalues is none!')

        for issue in issuevalues.keys():
            if (issuevalues[issue] == None):
                raise ValueError('value of issue: '+ issue + ' can not be none!')

        self.issuevalue = issuevalues

    def getIssues(self):
        return list(self.issuevalue)

    def getIssueNum(self):
        return len(self.issuevalue)

    def contianIssue(self, issue: str):
        return issue in self.issuevalue

    def getValue(self, issue: str):
        return self.issuevalue[issue]

    def update(self):
        pass

    def toString(self):
        pass

    def hashCode(self):
        pass  #hascode is to verify the unique of a bid.

    # partial bid not defined yet.

    def equals(self, bid):
        if isinstance(bid, Bid):
            return self.issuevalue == bid.issuevalue
        else:
            raise TypeError('input is not a bid!')