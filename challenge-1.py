def swapStrCase(string):
    for i in string:
        if i == i.lower():
            print(i.upper())
        else:
            print(i.lower())
        # if i.lower() == True:
        #     print(i.upper())
        # else:
        #     return string[i].lower()
        
        
swapStrCase('BaNana')