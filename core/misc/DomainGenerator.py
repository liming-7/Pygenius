import random
import json
from negotiator import BidIterator
import BidSpaceCash

def find_domain(domain, space_a, space_b, log_to_dir_a, log_to_dir_b, opp, dist, bias_for_high_opp, vary_both):
    """
    Method which keeps generating new domains until a domain satisfying the bounds
    on the opposition and bid distribution is found.


    @param domain: for which the profile should be generated
    @param space_a: preference profile of side A
    @param space_b: preference profile of side B
    @param log_to_dir_a: directory to log the new side A profile
    @param log_to_dir_b: directory to log the new side B profile
    @param opp: interval for opposition
    @param dist: interval for bid distribution
    @param bias_for_high_opp: bias search method to find domains with a high opposition faster
    @param vary_both: if false then solely a new preference profile for the B side is created

    """
    print("start to generate profile")
    result = []
    found = False
    while not found:
        if vary_both:
            space_a = randomize_util_space(space_a, bias_for_high_opp)
        space_b = randomize_util_space(space_b, bias_for_high_opp)
        result = calculate_distance(space_a, space_b)
        if result[0] in opp and result[1] in dist:
            found = True
        result = []
    if vary_both:
        write_json_to_file(space_a, log_to_dir_a)
    write_json_to_file(space_b, log_to_dir_b)


def randomize_util_space(utility_space, bias):
    """
    Method which randomizes a given utility space. If the bias parameter is true,
    then the result may be more likely to be a profile with a high oppositio.

    @param utility_space: profile to be randomized
    @param bias: towards domains with a high opposition
    @return: result of randomize
    """
    if bias:
        for index in utility_space.get_domain().get_issues():
            utility_space.set_weight(index, random.random())
        utility_space.normalize_children()
    else:
        for index in utility_space.get_domain().get_issues():
            utility_space.set_weight_simple(index, random.random())
        utility_space.normalize_children()

    for index in utility_space.get_evaluators():
        index.get_values().set_evaluation(
            utility_space.get_domain().get_random_bid().get_value(index.get_key().get_number()),
            int(random.random() * 1000))
    return utility_space


def calculate_distance(utility_space_a, utility_space_b):
    opposition = calculate_oppositions(utility_space_a, utility_space_b)
    bid_distribution = calculate_bid_distribution(utility_space_a, utility_space_b)
    result = [opposition, bid_distribution]
    return result


def write_json_to_file(content, log_path):
    file = open(log_path, "w")
    content = json.dumps(content.__dict__)
    file.write(content)
    file.close()


def calculate_bid_distribution(utility_space_a, utility_space_b):
    bid_list = BidIterator.create_bid_iterator(utility_space_a.get_domain())
    total = 0
    try:
        bid_space = BidSpaceCash.get_bid_space(utility_space_a,utility_space_b)
        if bid_space is not None:
            try:
                pass
            finally:
                pass
    finally:
        pass




def calculate_oppositions(utility_space_a, utility_space_b):
    pass
