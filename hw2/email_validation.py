import re

def fun(s):
    # your code here
    # return True if s is a valid email, else return False
    """
            Проверяет, является ли строка корректным email-адресом.

            Args:
                s (str): Email-адрес для проверки

            Returns:
                bool: True если email корректный, False если нет
            """
    # Разбиваем email на части
    try:
        username, rest = s.split('@')
        websitename, extension = rest.split('.')
    except ValueError:
        return False

    # Проверяем username (цифры, латинские буквы, тире, подчеркивания)
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False

    # Проверяем websitename (цифры и латинские буквы)
    if not re.match(r'^[a-zA-Z0-9]+$', websitename):
        return False

    # Проверяем extension (только латинские буквы, не более 3 символов)
    if not re.match(r'^[a-zA-Z]{1,3}$', extension):
        return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
