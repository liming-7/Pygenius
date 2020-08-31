# -*- coding: utf-8 -*-

#TODO:Doc and tests need to be completed.

class Domain:
    def __init__(self,json):
        try:
            self._name = json["name"]
            self._issuesValue = json["issuesValues"]
        except:
            print("Domain value format error!")
    def get_name(self) -> str:
        return self._name

    def get_issue_values(self) -> dict:
        return self._issuesValue
