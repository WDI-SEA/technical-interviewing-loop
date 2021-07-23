def total_chars(array):
    count = 0
    for element in array:
        new_thing = str(element)
        for i in new_thing:
            count = count + 1
    return(count)

# print(total_chars([25, "andie", 32, 3345, True])) 
