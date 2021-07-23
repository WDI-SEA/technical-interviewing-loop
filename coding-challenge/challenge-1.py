def swapStrCase(string):
    new_string = ""

    for i in string:
        if i.isupper():
            new_string += i.lower()
        else:
            new_string += i.upper()

    return new_string
