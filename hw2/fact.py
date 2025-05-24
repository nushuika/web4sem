import timeit

def fact_rec(n):
    if not isinstance(n, int):
        raise TypeError("Error!")
    if n < 1 or n > 10**5:
        raise ValueError("Error!")
    if n == 1:
        return 1
    return n * fact_rec(n - 1)


def fact_it(n):
    if not isinstance(n, int):
        raise TypeError("Error!")
    if n < 1 or n > 10**5:
        raise ValueError("Error!")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def compare_performance():
    n = 100
    rec_time = timeit.timeit(lambda: fact_rec(n), number=1000)
    it_time = timeit.timeit(lambda: fact_it(n), number=1000)

    print(f"\nПроизводительность для n={n}:")
    print(f"Рекурсивная версия: {rec_time:.6f} сек")
    print(f"Итеративная версия: {it_time:.6f} сек")

    if rec_time < it_time:
        print("\nРекурсивная версия работает быстрее")
    elif rec_time > it_time:
        print("\nИтеративная версия работает быстрее")
    else:
        print("\nОбе версии имеют схожую производительность")


if __name__ == '__main__':
    compare_performance()