def sum_and_sub(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Error!")

    sum_result = a + b
    sub_result = a - b

    return sum_result, sub_result

print(sum_and_sub(5, 3))
print(sum_and_sub(-2, 4))
