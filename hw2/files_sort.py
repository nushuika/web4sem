import argparse
import os
from collections import defaultdict


def get_sorted_files(directory):
    """
    Получает список файлов в директории, сгруппированных по расширению.

    Args:
        directory (str): Путь к директории

    Returns:
        dict: Словарь, где ключи - расширения файлов, значения - списки файлов
    """
    # Проверяем существование директории
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Директория '{directory}' не существует")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"'{directory}' не является директорией")

    # Группируем файлы по расширению
    files_by_ext = defaultdict(list)

    # Перебираем все файлы в директории
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Проверяем, что это файл (не директория)
        if os.path.isfile(filepath):
            # Получаем расширение (если есть) или пустую строку
            _, ext = os.path.splitext(filename)
            ext = ext.lower() if ext else ''

            # Добавляем файл в соответствующую группу
            files_by_ext[ext].append(filename)

    # Сортируем файлы внутри каждой группы
    for ext in files_by_ext:
        files_by_ext[ext].sort()

    return files_by_ext


def main():
    # Создаём парсер аргументов
    parser = argparse.ArgumentParser(
        description='Программа для вывода списка файлов в директории, сгруппированных по расширению'
    )

    # Добавляем обязательный аргумент - путь к директории
    parser.add_argument(
        'directory',
        help='Путь к директории для анализа'
    )

    # Получаем аргументы
    args = parser.parse_args()

    try:
        # Получаем отсортированные файлы
        files = get_sorted_files(args.directory)

        # Выводим результаты
        for ext in sorted(files.keys()):
            # Пропускаем пустое расширение, если оно есть
            if ext:
                print(f"\nРасширение '{ext}':")
            else:
                print("\nФайлы без расширения:")
            for filename in files[ext]:
                print(f"  {filename}")

    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Ошибка: {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())

#python3 files_sort.py C:\Users\Aisha\Desktop\web_dz