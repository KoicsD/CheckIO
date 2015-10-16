__author__ = 'KoicsD'


def det(num_pairs):
    return num_pairs[0][0] * num_pairs[1][1] - num_pairs[0][1] * num_pairs[1][0]

def diff(num_pair1, num_pair2):
    return (num_pair1[0] - num_pair2[0], num_pair1[1] - num_pair2[1])

def pos_vectors(num_pairs, origin):
    ret = []
    for pair in num_pairs:
        ret.append(diff(pair, origin))
    return ret

def rmv(lst, to_remove):
    ret = []
    for element in lst:
        if element != to_remove:
            ret.append(element)
    return ret

def is_winner(num_pairs):
    for pair in num_pairs:
        new_pairs = rmv(num_pairs, pair)
        positions = pos_vectors(new_pairs, pair)
        for i in range(len(positions)):
            for j in range(i):
                if det((positions[i], positions[j])) == 0:
                    return True
    return False

def get_num_pairs(game_result, ch):
    ret = []
    for i in range(3):
        for j in range(3):
            if game_result[i][j] == ch:
                ret.append((i, j))
    return ret

def checkio(game_result):
    x_pairs = get_num_pairs(game_result, "X")
    o_pairs = get_num_pairs(game_result, "O")
    if is_winner(x_pairs):
        return "X"
    elif is_winner(o_pairs):
        return "O"
    else:
        return "D"

if __name__ == '__main__':
    print(checkio([
        "OO.",
        "XOX",
        "XOX"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
