import random
import math


def circle_square_mk(r, n):
    """
    Вычисляет площадь окружности методом Монте-Карло.

    Args:
        r (float): радиус окружности
        n (int): количество экспериментов

    Returns:
        float: вычисленная площадь

    Raises:
        ValueError: если r <= 0 или n <= 0
    """
    # Проверяем корректность входных данных
    if r <= 0:
        raise ValueError("Error!")
    if n <= 0:
        raise ValueError("Error!")

    points_inside = 0

    # Генерируем n случайных точек в квадрате [-r, r] × [-r, r]
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)

        # Проверяем, попадает ли точка внутрь окружности
        if x ** 2 + y ** 2 <= r ** 2:
            points_inside += 1

    # Площадь окружности = (количество точек внутри) / (всего точек) * (площадь квадрата)
    return (points_inside / n) * (2 * r) ** 2