import os
import sys


def search_and_display_file(filename):

    # Получаем полный путь к файлу
    full_path = os.path.abspath(filename)

    try:
        # Открываем файл и читаем содержимое
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"\nФайл найден в директории: {os.path.dirname(full_path)}")
            print("\nПервые 5 строк файла:")
            print("-" * 40)
            # Показываем максимум 5 строк
            for i, line in enumerate(lines[:5], 1):
                print(f"{i}. {line.strip()}")

    except Exception as e:
        print(f"\nОшибка при чтении файла: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Использование: python file_search.py <имя_файла>")
        sys.exit(1)

    filename = sys.argv[1]
    search_and_display_file(filename)


if __name__ == "__main__":
    main()