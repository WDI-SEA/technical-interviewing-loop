'''
arr = [453, "hello", 293, True]
returns 15

variables:
    item_char_count
    total_char_count

iterate through array
    iterate though each array item
        return item char count
    add item char count to total
'''
arr = [453, "hello", 293, True]

def char_count(arr):
    char_count = 0
    for item in arr:
        item = (str(item))
        for _ in item:
            char_count += 1

    return(char_count)

print(char_count(arr))
            
