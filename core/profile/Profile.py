# -*- coding: utf-8 -*-
import collections
import Domain
import Bid

#TODO:Tests need to be completed.

#This file is not completed, not sure is required or not.

class Profile:
    def __init__(self, domain, name, bid):
        self._domain = domain
        self._name = name
        self._bid = bid

    def getDomain(self) -> Domain:
        return self._domain

    def getName(self) -> str:
        return self._name

    # Compare bid issue list and domain issue list, if they are same return True, if they are not same return false.
    def isComplete(self) -> bool:
        if collections.Counter(self._domain.get_issue_values().keys()) == collections.Counter(
                self._bid.get_issue_values().keys()):
            return True
        else:
            return False
