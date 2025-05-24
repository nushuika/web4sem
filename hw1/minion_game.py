def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in 'AEIOU':
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        return f"Kevin {kevin_score}"
    elif stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    else:
        return "Draw"

input_string = input("").strip()

if all(c.isupper() for c in input_string) and len(input_string) > 0:
    result = minion_game(input_string)
    print(result)
else:
    print("Error!")
