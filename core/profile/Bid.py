# -*- coding: utf-8 -*-

#TODO:Tests and doc need to be completed.


class Bid:
    # The issue_value is the dict of the {string:value}
    def __init__(self, issue_values):
        self._issueValues = issue_values

    # add another bid into the dictionary
    def addBid(self, issue, value):
        self._issueValues.update({issue: value})

    def getIssueValue(self, issue):
        return self._issueValues[issue]

    def getIssueValues(self):
        return self._issueValues

    def merge(self, other_bid):
        other_bid_dict = other_bid.getIssueValues()
        new_dict = self._issueValues
        new_dict = new_dict.update(other_bid_dict)
        return Bid(self, new_dict)

    def containsIssue(self, issue):
        return issue in self._issueValues.keys()
