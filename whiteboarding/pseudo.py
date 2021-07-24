# check if the difference between each strings length is > 1
# if yes, then they cannot be 1 away so instantly return False

# iterate through both strings at the "same speed" (i.e. start both at 0 and increment by 1 each loop)
# if we find matches then continue incrementing iters
# if we find that the characters don't match increase counter of changes
    # check if counter > 1 and if so return False

    # check if the string1[iter + 1] == string2[iter] and vice versa
    # this covers us if the only change is that we need to delete 1 character to match
    # if

# if we pass all of this then return True