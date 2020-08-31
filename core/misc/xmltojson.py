import json
import random
import os

import xmltodict
from functools import reduce


def change_domain_to_format(dict,domain_name):
    final_dict = {}
    dict = dict["negotiation_template"]["utility_space"]
    issueUtilities = dict["objective"]["issue"]
    issue_dict = create_domain_with_xml(issueUtilities)
    final_dict["issuesValues"] = issue_dict
    final_dict["name"] = domain_name
    return final_dict

def create_domain_with_xml(dict):
    final_dict = {}
    for index in dict:
        item_name = index["name"]
        value_list = []
        for index_inner in index["item"]:
            value_list.append(index_inner["value"])
        final_dict[item_name] = {"values":value_list}
    return final_dict

def change_dict_to_format(dict,name,domain_name):
    final_dict = {}
    dict = dict["utility_space"]
    issueUtilities = dict["objective"]["issue"]
    issue_list = change_issue_to_format(issueUtilities)
    weight_list = change_weight_to_format(dict["objective"]["weight"], issue_list)
    final_dict["issueWeights"] = weight_list
    domain_list = create_domain(issue_list, domain_name)
    final_dict["issueUtilities"] = issue_list
    final_dict["name"] = name
    final_dict["domain"] = domain_list
    bids_list = create_bid(domain_list)
    random.shuffle(bids_list)
    value_list,better = create_better(bids_list,issue_list,weight_list)
    temp_list = value_list.copy()
    temp_list.sort()
    final_dict["better"] = better
    final_dict["bids"] = bids_list
    position = int(0.25 * len(temp_list))
    bid_pos = value_list.index(temp_list[position])
    final_dict["reservationBid"] = bids_list[bid_pos]
    return {"LinearAdditiveUtilitySpace": final_dict}


def create_reservation(value, issue_util):
    # this function needs to be finished. we only have value in the xml file.
    pass

def create_better(bids_list,issue_list,weight_list):
    value_list = []
    better = []
    for index in bids_list:
        value_list.append(calc_value(index,issue_list,weight_list))
    for _ in range(20):
        bids_pick = random.sample(value_list,2)
        if bids_pick[1] > bids_pick[0]:
            bids_pick[0],bids_pick[1] = bids_pick[1],bids_pick[0]
        index = [value_list.index(bids_pick[0]),value_list.index(bids_pick[1])]
        better.append(index)
    return (value_list,better)

def create_bid(domain):
    issueValue = domain["issuesValues"]
    issue_name = []
    issue_list = []
    for index in issueValue.keys():
        issue = issueValue[index]
        issue_list.append(issue["values"])
        issue_name.append(index)
    result = lists_combination(issue_list,code="丨")
    result_list = []
    for index in result:
        temp_list = index.split("丨")
        temp = {}
        for flag in range(len(issue_name)):
            temp[issue_name[flag]] = temp_list[flag]
        result_list.append({"issuevalues":temp})
    return result_list

def lists_combination(lists, code=''):
    def myfunc(list1, list2):
        return [str(i)+code+str(j) for i in list1 for j in list2]
    return reduce(myfunc, lists)

def change_weight_to_format(dict, issue_list):
    issue_title = list(issue_list)
    result_dict = {}
    total = 0
    for index in range(len(dict)):
        #change here if you want to change the decimal of the float
        value = round(float(dict[index]["value"]),2)
        name = issue_title[index]
        print(total)
        if index == len(dict) -1:
            result_dict[name] = round(1 - total,2)
        else:
            total += value
            result_dict[name] = round(value,2)
    return result_dict


def create_domain(issue_list, name):
    domain_dict = {}
    issueValues = {}
    for index in issue_list.keys():
        if "discreteutils" in issue_list[index]:
            temp = create_discrete_domain(issue_list[index])
            issueValues[index] = temp
        else:
            temp = create_linear_domain(issue_list[index])
            issueValues[index] = temp
    domain_dict["name"] = name
    domain_dict["issuesValues"] = issueValues
    return domain_dict


def create_discrete_domain(dict):
    result_list = list(dict["discreteutils"]["valueUtilities"].keys())
    return {"values":result_list}


def create_linear_domain(dict):
    result_list = []
    result_list.append(dict["numberutils"]["lowValue"])
    result_list.append(dict["numberutils"]["highValue"])
    result_list.append(1)
    return {"range":result_list}


def change_issue_to_format(list):
    result_list = {}
    for index in list:
        if index["type"] == "discrete":
            temp = change_discreate_issue(index)
            result_list[temp[0]] = temp[1]
        else:
            temp = change_linear_issue(index)
            result_list[temp[0]] = temp[1]
    return result_list

def calc_value(bid,issue_uitl,weight):
    bid_list = bid["issuevalues"]
    util_list = issue_uitl
    total = 0.0
    for index in bid_list.keys():
        choice = bid_list[index]
        util = util_list[index]["discreteutils"]["valueUtilities"]
        total = total + util[choice] * weight[index]
    return total
def change_discreate_issue(dict):
    name = dict["name"]
    item_list = dict["item"]
    result_list = {}

    temp_list = []
    for index in item_list:
        temp_list.append(float(index["evaluation"]))
    maximum = max(temp_list)
    minimum = min(temp_list)
    for index in item_list:
        result_list[index["value"]] = round((float(index["evaluation"]) - minimum)/(maximum - minimum),2)
    valueUtils = {"valueUtilities": result_list}
    discreteutils = {"discreteutils": valueUtils}
    return (name, discreteutils)


def change_linear_issue(dict):
    name = dict["name"]
    lower_bound = int(dict["lowerbound"])
    upper_bound = int(dict["upperbound"])
    result_dict = {}
    result_dict["lowValue"] = lower_bound
    result_dict["highValue"] = upper_bound
    offset = float(dict["evaluator"]["offset"])
    slope = float(dict["evaluator"]["slope"])
    upset = offset + (upper_bound - lower_bound) * slope
    result_dict["lowUtility"] = offset
    result_dict["highUtility"] = upset
    result = {"numberutils":result_dict}
    return (name,result)


if __name__ == '__main__':
    file_path = "etc/ItexvsCypress/"
    path_list = os.listdir("templates/"+file_path)
    file_path = file_path.lower()
    domain_name = file_path.split("/")[-2].lower()
    print(domain_name)
    for index in path_list:
        file = open("templates/"+file_path+index, "rb")
        lines = file.read()
        result = xmltodict.parse(lines, attr_prefix="")
        temp = result.keys()
        index = index.strip(".xml")
        if "negotiation_template" in temp:
            result = change_domain_to_format(result,domain_name)
            print(domain_name)
            if not os.path.exists(os.path.dirname("temp/" + file_path + domain_name.replace("_","") + ".json")):
                try:
                    os.makedirs(os.path.dirname("temp/" + file_path + domain_name.replace("_","") + ".json"))
                except OSError as exc:  # Guard against race condition
                    print("error")
            with open("temp/" + file_path + domain_name.replace("_","") + ".json", 'w') as f:
                json.dump(result, f)
        else:
            result = change_dict_to_format(result,index.replace("_",""),domain_name)
            if not os.path.exists(os.path.dirname("temp/" + file_path + index.replace("_","") + ".json")):
                try:
                    os.makedirs(os.path.dirname("temp/" + file_path + index.replace("_","") + ".json"))
                except OSError as exc:  # Guard against race condition
                    print("error")
            with open("temp/" + file_path + index.replace("_","") + ".json", 'w') as f:
                json.dump(result, f)
        file.close()


