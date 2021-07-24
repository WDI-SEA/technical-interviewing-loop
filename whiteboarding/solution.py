def one_away(s1, s2):
    # check if the difference in size of each string is greater than 1
    if abs(len(s1) - len(s2)) > 1:
        # if true, then return False as this cannot be 1 edit away
        return False
    
    # setup iterators for both strings
    it1 = 0
    it2 = 0

    # track how many changes need to be made
    counter = 0

    # loop through each string and compare characters
    while it1 < len(s1) and it2 < len(s2):
        # check if letters are the same
        if s1[it1] == s2[it2]:
            # if true then move on to the next character in each
            it1 += 1
            it2 += 1
        else:
            # if letters are not the same increase the count
            counter += 1

            # if the counter is greater than 1 then strings are not 1 edit away
            if counter > 1:
                return False

            # check if the next character in s2 would match current s1
            if s1[it1] == s2[it2 + 1]:
                # if yes then move on to next s2
                it2 += 1
            # check if the next character in s1 would match current s2
            elif s1[it1 + 1] == s2[it2]:
                # if yes then move on to next s1
                it1 += 1
            else:
                # otherwise increase the iteration
                it1 += 1
                it2 += 1

    # if everything passes then return True
    return True

# print(one_away("pale", "ple"))
print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))