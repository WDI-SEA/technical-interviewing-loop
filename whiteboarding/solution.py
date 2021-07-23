def one_away(str1,str2):
    l1 = len(str1)
    l2 = len(str2)

    if abs(l1-l2) > 1:
        return False

    if l1 > l2:
        longer = list(str1)
        shorter = list(str2)
    else:
        longer = list(str2)
        shorter = list(str1)

    if l1 == l2:
        count = 0
        for i in range(l1):
            if longer[i] != shorter[i]:
                count += 1
            if count > 1:
                return False

    else:
        shift = 0
        for i in range(len(shorter)):
            if shorter[i] != longer[i+shift]:
                shift += 1
                if shift > 1 or shorter[i] != longer[i+shift]: return False

    return True