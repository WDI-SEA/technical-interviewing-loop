# In a language of your choosing, write a function which takes in an array of indeterminate size. Return the total number of individual characters in the passed-in array, regardless of variable data type. 


# Example: 

# arr = [453, "hello", 293, True]
# returns 15

def count_char(arr):
     count_char = 0
     for item in arr:
            item = (str(item))
            for _ in item:
                count_char += 1

     return(count_char)