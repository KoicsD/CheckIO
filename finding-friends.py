__author__ = 'KoicsD'


def multipop(list_of_lists, i):  # pops the 'i'th element from all the list in 'list_of_list'
    ret = []
    for lst in list_of_lists:
        ret.append(lst.pop(i))
    return ret


def find_isolateds_as_sets(network):  # collector function
    ret = []
    for first, second in [connection.split('-') for connection in network]:  # '-'-splitted list for connection-strings
        # we make a list of bools containing which isolated subgraphs contains the new nodes:
        # These subgraphs are represented by sets.
        first_in_set = [(first in set_of_drones) for set_of_drones in ret]
        second_in_set = [(second in set_of_drones) for set_of_drones in ret]
        # we decide if 'first' and 'second' node is contained by the graph at all:
        first_in_graph = True in first_in_set
        second_in_graph = True in second_in_set
        # and there are 4 cases:
        if first_in_graph and second_in_graph:  # both 'first' and 'second' node are contained
            # in this case we search for the two isolated subgraphs:
            i = first_in_set.index(True)
            if i == second_in_set.index(True):  # if these subgraphs/sets are the same,
                continue                        # there's nothing to do
            set_i = multipop([ret, first_in_set, second_in_set], i)[0]
            j = second_in_set.index(True)
            set_j = multipop([ret, first_in_set, second_in_set], j)[0]
            # and replace them with one single graph, the union of them:
            new_set = set.union(set_i, set_j)
            ret.append(new_set)
        elif first_in_graph:  # only the 'first' node is contained
            # in this case we add the second node to the same isolated subgraph:
            i = first_in_set.index(True)
            ret[i].add(second)
        elif second_in_graph:  # only the 'second' node is contained
            # in this case we add the first node to the same subgraph similarly:
            i = second_in_set.index(True)
            ret[i].add(first)
        else:  # neither is contained
            # in this case we mark them as a new isolated subgraph:
            ret.append({first, second})
    return ret  # we return the list of subgraphs (sets)


def check_connection(network, first, second):
    # we collect the isolated subgraphs in a list of sets of strings:
    isolated_graphs = find_isolateds_as_sets(network)
    # now it's enough to decide if the set of the 2 given drones is a subset of any of the sets above:
    return True in [graph.issuperset({first, second}) for graph in isolated_graphs]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
