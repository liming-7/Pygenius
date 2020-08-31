from functools import reduce
import matplotlib.pyplot as plt
import json
import numpy as np
import math
import xmltojson

def calculate(bid, profile):
    utilities = profile["LinearAdditiveUtilitySpace"]
    weight = utilities["issueWeights"]
    utility_profile = utilities["issueUtilities"]
    if bid == "":
        bid = utilities["reservationBid"]
    bid_list = bid["issuevalues"]
    index = 0
    value_list = {}
    for index in bid_list.keys():
        temp_utility = utility_profile[index]
        value = temp_utility["discreteutils"]["valueUtilities"][bid_list[index]]
        value_list[index] = value
    final_result = 0
    for index in value_list.keys():
        final_result += weight[index] * value_list[index]
    return round(final_result, 2)


def get_pareto_frontier(domain, profile1, profile2):
    bid_list = xmltojson.create_bid(domain)
    bid_pair = []
    for bid in bid_list:
        x = calculate(bid, profile1)
        y = calculate(bid, profile2)
        bid_pair.append((x, y))
    frontier = []
    # show the data point on the graph
    # x_ray = []
    # y_ray = []
    # for index in bid_pair:
    #     x_ray.append(index[0])
    #     y_ray.append(index[1])
    # plt.scatter(x_ray, y_ray)
    #
    # my_x_ticks = np.arange(0, 1, 0.1)
    # my_y_ticks = np.arange(0, 1, 0.1)
    # plt.xticks(my_x_ticks)
    # plt.yticks(my_y_ticks)
    # plt.show()
    #
    for index in bid_pair:
        x = index[0]
        y = index[1]
        flag = True
        for inner_index in frontier:
            if inner_index[0] >= x and inner_index[1] >= y:
                flag = False
            if inner_index[0] <= x and inner_index[1] <= y:
                frontier.remove(inner_index)
                continue
        if flag:
            frontier.append(index)
    # show the point on the graph
    # x_ray = []
    # y_ray = []
    # for index in frontier:
    #     x_ray.append(index[0])
    #     y_ray.append(index[1])
    # plt.scatter(x_ray,y_ray)
    #
    # my_x_ticks = np.arange(0, 1, 0.1)
    # my_y_ticks = np.arange(0, 1, 0.1)
    # plt.xticks(my_x_ticks)
    # plt.yticks(my_y_ticks)
    # plt.show()
    #
    return frontier


def calculate_nash_point(profile1, profile2, frontier):
    x_value = calculate("",profile1)
    y_value = calculate("",profile2)
    max_distance = 0
    point = frontier[0]
    for index in frontier:
        x = index[0] - x_value
        y = index[1] - y_value
        if x * y > max_distance:
            max_distance = x * y
            point = index
    return point


def calculate_distance_to_nash_point(point, nash_point):
    x = nash_point[0] - point[0]
    y = nash_point[1] - point[1]
    return math.sqrt(x * x + y * y)


def calculate_distance_to_frontier(point, frontier):
    minimum = 1
    for index in frontier:
        x = index[0] - point[0]
        y = index[1] - point[1]
        distance = math.sqrt(x * x + y * y)

        if distance < minimum:
            minimum = distance
    return minimum


def calculate_frontier_and_nash(domain, profile1, profile2, temp_bid):
    frontier = get_pareto_frontier(domain, profile1, profile2)
    x = calculate(temp_bid, profile1)
    y = calculate(temp_bid, profile2)
    bid_point = (x, y)
    frontier_distance = calculate_distance_to_frontier(bid_point, frontier)
    nash_point = calculate_nash_point(profile1, profile2, frontier)
    nash_distance = calculate_distance_to_nash_point(bid_point, nash_point)
    return frontier_distance, nash_distance

#TODO: finish the warfare point function
def calculate_walfare_point():
    pass

