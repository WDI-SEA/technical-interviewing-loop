def charCounter(list):
    answer_list = []

    for item in list:
        answer_list.append(str(item))

    answer = f"This list has {len(''.join(answer_list))} character"

    if len(''.join(answer_list)) == 1:
        return answer + "."
    return answer + "s."
    


print(charCounter([453, "hello", 293, True]))