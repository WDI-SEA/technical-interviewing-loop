def swapStrCase(string):
    # return swapcase(string)
    new_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                char = char.capitalize()
            elif char.isupper():
                char = char.lower()
        new_string += char
    return new_string