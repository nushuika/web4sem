import argparse


def my_sum(*args):
    """
    Функция для сложения произвольного количества аргументов.

    Args:
        *args: Любое количество числовых аргументов

    Returns:
        float: Сумма всех переданных чисел

    Raises:
        TypeError: Если хотя бы один аргумент не является числом
    """
    # Проверка типа всех аргументов
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError("Error! Все аргументы должны быть числами")

    # Суммирование всех аргументов
    return sum(args)


def main():
    # Создаём парсер аргументов
    parser = argparse.ArgumentParser(
        description='Программа для сложения чисел, переданных как аргументы командной строки'
    )

    # Добавляем позиционные аргументы
    parser.add_argument(
        'numbers',
        type=float,
        nargs='+',
        help='Числа для сложения'
    )

    # Получаем аргументы
    args = parser.parse_args()

    try:
        # Вычисляем сумму и выводим результат
        result = my_sum(*args.numbers)
        print(result)
    except TypeError as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()

#python3 my_sum_argv.py 1 2 3 4 5