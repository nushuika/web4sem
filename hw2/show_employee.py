def show_employee(name, salary=100000):
    if not name:
        raise ValueError("Error!")

    if not isinstance(salary, (int, float)):
        raise TypeError("Error!")

    if salary < 0:
        raise ValueError("Error!")

    return f"{name}: {salary} ₽"

print(show_employee("Gazimagomedova Aisha"))
print(show_employee("Sanaya Ilya", 150000))