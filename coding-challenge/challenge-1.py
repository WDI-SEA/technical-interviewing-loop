def swapStrCase(string):
    new_string = ""
    for letter in string:
        if letter.isupper() is True:
            letter = letter.lower() 
        else:
            letter = letter.upper()
        new_string+= letter
    return(new_string)

# print(swapStrCase("ANDrea"))