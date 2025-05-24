def my_sum(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError("Error!")

    return sum(args)

print(my_sum(1, 2, 3, 4, 5))
