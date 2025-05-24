n = int(input(""))
A = list(map(int, input("").split()))
if len(A) != n:
        print("Error!")
else:
    scores = set(A)
    if len(scores) < 2:
        print("Error!")
    else:
        sorted_scores = sorted(scores, reverse=True)
        second_place = sorted_scores[1]
        print(second_place)
