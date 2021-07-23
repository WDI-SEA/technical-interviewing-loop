def swapStrCase(str):
    answer = ""
    for char in str:
        if char.isupper() == True:
            answer += char.lower()
        else:
            answer += char.upper()
    return answer
        

print(swapStrCase("Hello World"))