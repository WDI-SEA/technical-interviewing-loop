# def char count to count chars, set it to 0
def char_count(arr):
    chars = 0

    # for each string, add the string length to chars
    for i in arr:
        chars += len(str(i))

    # return chars
    return chars

arr = [453, "hello", 293, True]

print(char_count(arr)) 