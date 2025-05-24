import time
import random

def process_list(arr):
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_comprehension(arr):
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    for i in arr:
        if i % 2 == 0:
            yield i**2
        else:
            yield i**3

arr = [random.randint(1, 100) for _ in range(10000)]

start_time = time.time()
process_list(arr)
list_time = time.time() - start_time

start_time = time.time()
process_list_comprehension(arr)
comprehension_time = time.time() - start_time

start_time = time.time()
list(process_list_gen(arr))
gen_time = time.time() - start_time

print(f"Время работы оригинальной функции: {list_time:.6f} секунд")
print(f"Время работы функции с list comprehension: {comprehension_time:.6f} секунд")
print(f"Время работы функции-генератора: {gen_time:.6f} секунд")