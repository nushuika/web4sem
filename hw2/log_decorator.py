import logging
import functools
from datetime import datetime


def function_logger(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Получаем текущее время
            start_time = datetime.now()

            # Логируем информацию о вызове функции
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f"{func.__name__}\n")
                file.write(f"{start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}\n")

                # Логируем позиционные и ключевые аргументы
                if args:
                    file.write(f"{args}\n")
                if kwargs:
                    file.write(f"{kwargs}\n")

                # Вызываем функцию
                result = func(*args, **kwargs)

                # Логируем результат
                if result is None:
                    file.write("-\n")
                else:
                    file.write(f"{result}\n")

                # Логируем время завершения и время работы функции
                end_time = datetime.now()
                file.write(f"{end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}\n")
                execution_time = end_time - start_time
                file.write(f"{execution_time}\n\n")

            return result

        return wrapper

    return decorator


# Пример использования
@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'


greeting_format('John')
