def chall_three (array) :
    count = 0
    for i in array:
        # print(type(i))
        if type(i) == str:
            count += len(i)
        else:
            count += len(str(i))
        #     count += len(i)
        # else:
        #     count += len(i)
    
    print(count)
    
    
arr = [453, "hello", 293, True]
chall_three(arr)
