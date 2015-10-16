__author__ = 'KoicsD'


def lower_left(pawn):
    ret = ""
    ret += chr(ord(pawn[0]) - 1)
    ret += chr(ord(pawn[1]) - 1)
    return ret


def lower_right(pawn):
    ret = ""
    ret += chr(ord(pawn[0]) + 1)
    ret += chr(ord(pawn[1]) - 1)
    return ret


def collect_insurance_fields(pawn):  # collects fields that can provide safety for field 'pawn'
    ret = set()
    if pawn[0] != 'a':
        ret.add(lower_left(pawn))
    if pawn[0] != 'h':
        ret.add(lower_right(pawn))
    return ret


def pawn_safe(pawn, pawns):  # decides if 'pawn' is in safe by any of 'pawns'
    if pawn[1] == '1':  # if number is 1,
        return False    # there is no lower rank to provide safety
    # let's collect the fields that can provide safety:
    guard = collect_insurance_fields(pawn)
    # we only need to check if at least one of them is in 'pawns':
    return not set.isdisjoint(guard, pawns)


def safe_pawns(pawns):
    # it's a simple counter
    count = 0
    for pawn in pawns:
        if pawn_safe(pawn, pawns):
            count += 1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
