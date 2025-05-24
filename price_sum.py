def aggregate_data(filename="products.txt"):
    adult_sum = 0
    retired_sum = 0
    child_sum = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            next(file)

            for line in file:
                parts = line.strip().split(',')
                adult_sum += float(parts[1].replace(',', '.'))
                retired_sum += float(parts[2].replace(',', '.'))
                child_sum += float(parts[3].replace(',', '.'))
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"

    return f"{adult_sum:.2f} {retired_sum:.2f} {child_sum:.2f}"

if __name__ == "__main__":
    result = aggregate_data()
    print(result)
