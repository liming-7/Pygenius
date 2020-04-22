# -*- coding: utf-8 -*-

"""
The class for the issue utilities.
t can calculate the utility result and return the utility list for a specific value.
"""

#TODO:Tests need to be completed.
class IssueUtilities:

    # Init the class, print error if data structure is not correct.
    def __init__(self, json):
        try:
            self._issueUtilities = json["discreteutils"]
        except:
            print("Issue utilities got wrong data structure")

    # Get utility list for a value. Return None if this value does not exist.
    def getUtility(self, value):
        if value in self._issueUtilities:
            return self._issueUtilities[value]
        else:
            return None

    # Calculate the utilities score of bid. input should be [bid:weight] and follow the index of the issue utilities.
    # input the weight, issue, and bid result into this function and it will return the result of calculation.
    def calcualteUtility(self, issue, weight, bid):
        try:
            bid_dict = self._issueUtilities[issue]
            bid_value = bid_dict[bid]
            result = weight * bid_value
            return result
        except:
            print("No such issue")
            return None
