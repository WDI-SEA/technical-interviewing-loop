def count_char(arr):
    total = 0

    for i in arr:
        total += len(str(i))
    
    return total

arr = [453, "hello", 293, True]

count_char(arr)