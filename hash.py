list1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def smallest(key):

    total = 0 

    for arr in list1:
        smallest_val = min(arr)
        total += smallest_val
    return total


print(smallest(list1))