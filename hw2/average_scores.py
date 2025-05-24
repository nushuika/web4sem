def compute_average_scores(scores):
    n = len(scores[0])
    if not 0 < n <= 1000:
        raise ValueError(f"Количество студентов должно быть больше 0 и не превышать 1000, получено {n}")

    x = len(scores)
    if not 0 < x <= 100:
        raise ValueError(f"Количество предметов должно быть больше 0 и не превышать 100, получено {x}")

    for subject_scores in scores:
        for score in subject_scores:
            if score > 100:
                raise ValueError(f"Оценка {score} превышает максимально допустимое значение 100")
            if score < 0:
                raise ValueError(f"Оценка {score} не может быть отрицательной")

    student_scores = []

    for i in range(n):
        student_scores.append([score[i] for score in scores])

    averages = []
    for student in student_scores:
        avg = sum(student) / len(student)
        averages.append(round(avg, 1))

    return tuple(averages)


def main():
    try:
        n, x = map(int, input().split())
    except ValueError:
        print("Ошибка: N и X должны быть целыми числами")
        return

    scores = []
    try:
        for _ in range(x):
            scores.append(tuple(map(float, input().split())))
    except ValueError:
        print("Ошибка: Оценки должны быть числами")
        return

    try:
        averages = compute_average_scores(scores)
        for avg in averages:
            print(avg)
    except ValueError as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()