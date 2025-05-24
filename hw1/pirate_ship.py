class Cargo:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight  # Стоимость за единицу веса


def pirate_ship(n, m, cargo_list):
    # Сортируем грузы по стоимости за единицу веса в порядке убывания
    cargo_list.sort(key=lambda x: x.value_per_weight, reverse=True)

    total_weight = 0  # Общий вес груза
    total_value = 0  # Общая стоимость груза
    result = []  # Список для хранения результатов

    for cargo in cargo_list:
        if total_weight < n:  # Если ещё есть место на корабле
            if total_weight + cargo.weight <= n:  # Если груз помещается целиком
                total_weight += cargo.weight
                total_value += cargo.value
                result.append(f"{cargo.name} {cargo.weight} {cargo.value:.2f}")
            else:  # Если груз не помещается целиком, берем часть груза
                remaining_capacity = n - total_weight
                partial_value = (remaining_capacity / cargo.weight) * cargo.value
                total_weight += remaining_capacity
                total_value += partial_value
                result.append(f"{cargo.name} {remaining_capacity:.2f} {partial_value:.2f}")

    return result


# Чтение входных данных
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    cargo_list = []

    for _ in range(m):
        line = input().strip().split()
        name = line[0]
        weight = int(line[1])
        value = int(line[2])
        cargo_list.append(Cargo(name, weight, value))

    result = pirate_ship(n, m, cargo_list)

    # Вывод результата в порядке убывания стоимости
    for item in result:
        print(item)

#50 3
#Золото 10 60
#Алмазы 20 100
#Медь 30 120
