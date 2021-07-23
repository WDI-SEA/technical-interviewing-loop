# brute-forceishS

# function takes 2 strings, str1 and str2
    # first get difference in lengths:
        # if greater than 1 (or less than -1?): return false
    
    # here we can cast to lists for easier iteration
    # check which is longer for later

    #if same length loop through and compare:
        # count differences, if greater than 1 return false
    
    # else if lengths off by 1, loop through shorter string:
    # increment on i, track a shift that starts at 0
        # like  if short_str[i] == long_str[i+shift]
        # if chars are different:
            # increment shift
            # if shift > 1 return false
            # compare again with new shift
                # if different return false

    # if you get through all that, return true