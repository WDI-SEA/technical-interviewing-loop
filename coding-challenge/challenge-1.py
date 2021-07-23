def swapStrCase(string):
    answer = ""
    for char in string:
        if char.isupper() == True:
            answer += char.lower()
        else:
            answer += char.upper()
    return answer
        