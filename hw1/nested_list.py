while True:
        N = int(input())
        if 2 <= N <= 5:
            break
        else:
            print("Error!")

names = input().split()

while True:
        scores = list(map(float, input().split()))
        if len(scores) == N:
            break
        else:
            print("Error!")

students = list(zip(names, scores))

unique_scores = sorted(set(score for name, score in students))
if len(unique_scores) > 1:
    second_highest_score = unique_scores[1]
    names_with_second_highest = [name for name, score in students if score == second_highest_score]
    names_with_second_highest.sort()
    for name in names_with_second_highest:
        print(name)
else:
    print("Error!")
