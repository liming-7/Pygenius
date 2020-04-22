# -*- coding: utf-8 -*-
# @Time    : 06/04/2020 11:53
# @Author  : Ming Li
# @FileName: utilityspace.py
# @Software: PyCharm

"""
Defines an UtilitySpace in terms of a weighted sum of per-issue preferences.
"""

# TODO: Doc needs to be completed, tests need to be completed. Jobs2.json is temp for testing, it seems to work. Need
# further testing.

import json
import Domain
import Bid


class UtilitySpace:
    """
    def getUtilities(self) -> dict:
        return self._utilitiles


    def getWeights(self) -> dict:
        return self._weights

    def getWeight(self) -> float:
        return self._Weight
    """

    def __init__(self, json):
        try:
            content = json["LinearAdditiveUtilitySpace"]
            self._issueUtilities = content["issueUtilities"]
            self._name = content["name"]
            reservationBid = content["reservationBid"]
            self._reservationBid = Bid.Bid(reservationBid)
            domain = content["domain"]
            self._domain = Domain.Domain(domain)
            self._issueWeights = content["issueWeights"]

        except:
            print("Wrong data structure!")

    def getName(self) -> str:
        return self._name

    def getDomain(self):
        return self._domain

    def getIssueUtilities(self) -> list:
        return self._issueUtilities

    def getReservationBid(self):
        return self._reservationBid

    def getIssueWeights(self):
        return self._issueWeights


if __name__ == '__main__':
    f = open("jobs2.json")
    data = json.load(f)
    object = UtilitySpace(data)
    print(object.getName())
    print(object.getDomain())
    print(object.getReservationBid())
    print(object.getIssueUtilities())
    f.close()
