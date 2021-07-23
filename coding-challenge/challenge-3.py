"""
In a language of your choosing, write a function which takes in an array of indeterminate size. Return the total number of individual characters in the passed-in array, regardless of variable data type. 


Example: 
arr = [453, "hello", 293, True]
returns 15

"""

arr = [453, "hello", 293, True]
x = 0
for item in arr:

    for char in str(item):
        x +=1
print(x)





