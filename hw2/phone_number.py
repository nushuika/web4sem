def normalize_phone(phone):
    """
    Приводит телефонный номер к единому формату без префиксов
    """
    # Удаляем все нецифровые символы
    digits_only = ''.join(filter(str.isdigit, phone))

    # Если номер начинается с 8, заменяем на 7
    if digits_only.startswith('8'):
        digits_only = '7' + digits_only[1:]

    # Если номер начинается с 0, удаляем его
    if digits_only.startswith('0'):
        digits_only = digits_only[1:]

    # Добавляем префикс +7 если он отсутствует
    if not digits_only.startswith('7'):
        digits_only = '7' + digits_only

    return digits_only


def format_phone(phone):
    """
    Форматирует телефонный номер в требуемый вид
    """
    # Получаем чистый номер без префикса
    digits = phone[1:]

    # Форматируем по шаблону
    return f"+7 ({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"


def wrapper(f):
    def fun(l):
        # Преобразуем каждый номер в список [нормализованный_номер, отформатированный_номер]
        formatted_numbers = []
        for phone in l:
            # Нормализуем номер для сортировки
            normalized = normalize_phone(phone)
            # Форматируем номер для вывода
            formatted = format_phone(normalized)
            formatted_numbers.append((normalized, formatted))

        # Сортируем по нормализованному номеру
        sorted_numbers = f([x[0] for x in formatted_numbers])

        # Возвращаем отформатированные номера в том же порядке, что и отсортированные
        return [formatted for _, formatted in zip(sorted_numbers, formatted_numbers)]

    return fun


@wrapper
def sort_phone(l):
    return sorted(l)


if __name__ == '__main__':
    n = int(input())
    phones = []

    # Читаем все номера
    for _ in range(n):
        phones.append(input().strip())

    # Сортируем и выводим результаты
    formatted_numbers = sort_phone(phones)
    print(*formatted_numbers, sep='\n')