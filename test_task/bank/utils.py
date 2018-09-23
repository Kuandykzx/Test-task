
def withdraw_rec(notes, amount, keys, index, result=None):
    """
    Basic logic is : going through reverse sorted keys from high to low -> index
    take highest key s that is lower than amount: then go further 3 cases
        1. take this s from amount, and repeat
        2. take this s from amount, go to next lower key
        3. do not take s from amount, go to next lower key

    :param notes: all banknotes
    :param amount: amount to be equal
    :param keys: key list in reversed sorted order
    :param index: index of current note in key list
    :param result: resulting dict
    :return: result dict or None
    """

    if result is None:
        result = {}

    if index >= len(keys):
        return None

    if amount == 0:
        return result
    key = keys[index]
    val = notes[key]

    if key > amount or val < 1:
        return withdraw_rec(notes, amount, keys, index+1, result)
    else:
        notes[key] = val-1
        if key in result.keys():
            result[key] += 1
        else:
            result[key] = 1

        case_1 = withdraw_rec(notes, amount-key, keys, index, result)
        if case_1: return case_1
        case_2 = withdraw_rec(notes, amount-key, keys, index+1, result)
        if case_2: return case_2
        notes[key] = val
        result[key] = result[key]-1
        case_3 = withdraw_rec(notes, amount, keys, index+1, result)
        if case_3: return case_3
        return None


def withdraw_money(notes, amount):
    """

    :param notes: all banknotes
    :param amount: amount to equal
    :return: withdrawal dictionary or None
    """
    data = []
    for key in sorted(notes.keys(), reverse=True):
        data.append(key)

    res = withdraw_rec(notes, amount, data, 0)
    return res