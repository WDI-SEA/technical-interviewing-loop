# Set up initial class Solution
class Solution:
    # Def function
    def isOneEditDistance(self, w1: str, w2:str) -> bool:

     # Check to make sure strings only vary by one letter
        if abs(len(w1) - len(w2)) > 1:
            return False
    
    # Ensure w2 is the shorter of the two strings
        if len(w2) > len(w1):
            
            # Reverse order if true
            w1, w2 = w2, w1

        # Kepp track of umber of incorrect letters, start at 0
        inc = 0

        # Loop over w1 with i and w2 with j, set both equal to 0
        i = 0
        j = 0

        # Loop for while j < length of w2
        while j < len(w2):
        
            # Check if the indexes between the two words do not match
            if w1[i] != w2[j]:
                
                # Found an inc letter, increment counter
                inc += 1
                
                # Check if wrong > 1, return False if so
                if inc > 1:
                    return False
                
                # Move to next char in longer string
                i += 1
                
                # If both strings are strictly the same length, move forward in shorter string.
                # If not, don't move in the shorter string -- this covers the case 
                # of an extra letter.
                if len(w1) == len(w2):
                    j += 1
            # Else if indexes match, move to next letter in both
            else: 
                i += 1
                j += 1

        # Return true
        return True