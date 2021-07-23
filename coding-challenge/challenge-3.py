
#In a language of your choosing, write a 
# function which takes in an array of
#  indeterminate size. Return the total 
# number of individual characters in the 
# passed-in array, regardless of variable 
# data type. 



arr = [453, "hello", 293, True]
#returns 15

def indv_char(arr):
    counter = 0
    for i in arr:
        if type(i) == str:
            for x in i:
                counter += 1
        else:
            string = str(i)
            for x in string:
                counter += 1
            
    print(counter)

indv_char(arr)


