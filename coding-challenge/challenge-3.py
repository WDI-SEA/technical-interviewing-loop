def count_chars(arr):
    count = 0
    for elem in arr:
        if type(elem) is str:
            count += len(elem)
        elif type(elem) is int or type(elem) is float:
            count += len(str(elem))
        elif type(elem) is bool:
            if elem:
                count += 4
            else:
                count += 5
        elif type(elem) is list or type(elem) is tuple or type(elem) is set:
            count += count_chars(elem)
    return count