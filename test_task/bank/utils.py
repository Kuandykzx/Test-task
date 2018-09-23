def withdraw_rec(notes, amount, keys, index, result=None):
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
    data = []
    for key in sorted(notes.keys(), reverse=True):
        data.append(key)

    res = withdraw_rec(notes, amount, data, 0)
    return res