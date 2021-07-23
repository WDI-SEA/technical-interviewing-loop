# Set up initial class Solution
    # Def function, use w1 and w2 for strings
        # Check to make sure strings only vary by one letter
        # Ensure w2 is the shorter of the two strings
            # Reverse order if true
        # Keep track of umber of incorrect letters, start at 0
        # Loop over w1 with i and w2 with j, set both equal to 0
        # Loop for while j < length of w2
            # Check if the indexes between the two words do not match
                # Found an inc letter, increment counter
                # Check if wrong > 1, return False if so
                # Move to next char in longer string
                
                # If both strings are strictly the same length, move forward in shorter string.
                # If not, don't move in the shorter string -- this covers the case 
                # of an extra letter.
            # Else if indexes match, move to next letter in both
        # Return True


